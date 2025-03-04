from flask import Flask, request, render_template
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import groq

# ---- Hardcoded Confluence & API Credentials ---- #
CONFLUENCE_URL = "https://mukeshanbazhagan.atlassian.net/wiki/rest/api/content/"
EMAIL = "mukeshanbazhagan@gmail.com"
API_TOKEN = "ATATT3xFfGF0K4zkk7a-Hdd5Kx8FEZ67cR4pwmpIi9yzYOJ1cn1uB5eBArJ5K77ELQnT7uJH0TbM_TIZ2Fqw-Oq68uTciVqpCtvyFVk_Cq826k3ExYfGW6JylYDuzeeNhNwbFmS0T-iP495wIIBRIdZ3JcQEMxUYGYPCSmpJQSSKNh6CH76d_a8=97EBC594"
GROQ_API_KEY = "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"

app = Flask(__name__)

# ---- Fetch All Confluence Pages ---- #
def get_confluence_pages():
    url = f"{CONFLUENCE_URL}?expand=body.storage"
    response = requests.get(url, auth=HTTPBasicAuth(EMAIL, API_TOKEN), headers={"Content-Type": "application/json"})
    
    if response.status_code == 200:
        pages = response.json().get("results", [])
        return [{"id": page["id"], "title": page["title"]} for page in pages]
    else:
        return []

# ---- Fetch Selected Page Content ---- #
def fetch_confluence_page(page_id):
    url = f"{CONFLUENCE_URL}/{page_id}?expand=body.storage"
    response = requests.get(url, auth=HTTPBasicAuth(EMAIL, API_TOKEN), headers={"Content-Type": "application/json"})
    
    if response.status_code == 200:
        data = response.json()
        return data["body"]["storage"]["value"]
    else:
        return f"Error: {response.status_code} {response.text}"

# ---- Extract Text from HTML ---- #
def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    return soup.get_text(separator="\n").strip()

# ---- AI Chatbot Response ---- #
def get_ai_response(question, document):
    client = groq.Client(api_key=GROQ_API_KEY)
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are an AI assistant for Confluence pages."},
            {"role": "user", "content": f"Based on this document:\n\n{document[:4000]}\n\nAnswer this question: {question}"}
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content

# ---- Web Interface ---- #
@app.route("/", methods=["GET", "POST"])
def index():
    pages = get_confluence_pages()  # Fetch all pages for dropdown
    selected_page_id = None
    previous_qa = []  # Store previous questions & answers
    
    if request.method == "POST":
        selected_page_id = request.form.get("page_id")  # Keep selected page
        question = request.form.get("question")
        
        page_html = fetch_confluence_page(selected_page_id)
        if "Error" in page_html:
            return render_template("index.html", error=page_html, pages=pages, selected_page_id=selected_page_id, previous_qa=previous_qa)

        page_text = extract_text_from_html(page_html)
        answer = get_ai_response(question, page_text)
        
        previous_qa.append({"question": question, "answer": answer})  # Store Q&A
        
        return render_template("index.html", question=question, answer=answer, page_id=selected_page_id, pages=pages, selected_page_id=selected_page_id, previous_qa=previous_qa)

    return render_template("index.html", pages=pages, selected_page_id=selected_page_id, previous_qa=previous_qa)

if __name__ == "__main__":
    app.run(debug=True)
