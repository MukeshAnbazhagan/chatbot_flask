# Confluence AI Chatbot

This project is a **Flask-based AI chatbot** that fetches Confluence pages, processes their content, and answers user questions using Groq's AI model. The app is deployed on **Render**.

## Features
- Fetches Confluence pages using Atlassian REST API
- Extracts text content from Confluence pages
- Uses **Groq's LLaMA 3** model to generate AI-powered responses
- Web UI to interact with Confluence data
- Deployed on **Render**

## Tech Stack
- **Python** (Flask, Requests, BeautifulSoup)
- **Groq API** for AI-powered responses
- **Render** for deployment
- **Atlassian Confluence API** for data fetching

---

## Installation

### Clone the Repository
```bash
git clone https://github.com/yourusername/confluence-ai-chatbot.git
cd confluence-ai-chatbot
```

### Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Up Environment Variables
Create a `.env` file in the root directory:
```
CONFLUENCE_EMAIL=your_email@example.com
CONFLUENCE_API_TOKEN=your_api_token
GROQ_API_KEY=your_groq_api_key
```

---

## Run the Flask App Locally
```bash
python app.py
```
The app will be available at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Deployment on Render

### Push Your Code to GitHub
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

### Deploy to Render
- Go to **Render Dashboard** → Create a New Web Service
- Connect to your GitHub repository
- Set **Build Command**: `pip install -r requirements.txt`
- Set **Start Command**: `gunicorn -w 4 -b 0.0.0.0:$PORT app:app`
- Add environment variables (`.env` values) in Render's **Environment Variables** section

###  Get Your Public URL
After deployment, Render will provide a public URL like:
```
https://your-app.onrender.com
```
Use this link to access the chatbot.

---

##  API Endpoints

| Method | Endpoint | Description |
|--------|----------|--------------|
| `GET`  | `/` | Load the chatbot UI |
| `POST` | `/` | Ask a question about a Confluence page |

---

##  Notes
- Keep your **API keys secure** and do **NOT** commit `.env` to GitHub.
- Use **gunicorn** for production deployment on Render.

---

##  Future Enhancements
- Add authentication for secure access
- Improve UI with React or Flask templates
- Integrate with Slack or Teams for direct chat support

### If you find this project helpful, consider starring it on GitHub!

---

📧 **Contact:** [mukeshanbazhagan@gmail.com]  | 🌐 **GitHub:** [https://github.com/MukeshAnbazhagan/]

