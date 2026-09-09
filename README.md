# 📚 Active Reading Sandbox

An AI-powered document tutor that transforms passive reading into an interactive learning experience. Built with **FastAPI**, **Vanilla JS/TailwindCSS**, and the **Google Gemini 3.5 Flash** model.

## ✨ Features
- **Upload & Read:** Seamlessly upload PDF documents and view extracted text.
- **AI Tutor:** Ask questions, request summaries, or generate quizzes based specifically on the uploaded document context.
- **Real-Time Streaming:** Responses are streamed token-by-token for a fast, responsive user experience.
- **Dual Deployment:** Run locally via Python/Uvicorn or containerize with Docker.

## 📁 Project Structure
```text
active-reading-sandbox/
├── docker-compose.yml     # Docker Compose configuration
├── Dockerfile             # Docker image instructions
├── requirements.txt       # Python dependencies
├── main.py                # FastAPI backend & Gemini integration
└── static/
    └── index.html         # Frontend UI
```

## 🚀 Getting Started

### Prerequisites
- A [Google Gemini API Key](https://aistudio.google.com/app/apikey)
- Python 3.10+ (If running manually)
- Docker Desktop (If running via Docker)

### Option 1: Run with Docker (Recommended)
1. Clone or download this repository.
2. Open your terminal in the project folder.
3. Run the following command:
   ```bash
   docker compose up --build
   ```
4. Open your browser and go to `http://localhost:8000`.

### Option 2: Run Manually (Python)
1. Open your terminal in the project folder.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the FastAPI server (using the module command to avoid PATH issues):
   ```bash
   python -m uvicorn main:app --host 0.0.0.0 --port 8000
   ```
4. Open your browser and go to `http://localhost:8000`.

## 🔑 Configuring the API Key
You can provide your Gemini API key in one of three ways:
1. **Web UI:** Enter it in the top-right corner of the application before uploading a document.
2. **Docker Compose:** Add your key to the `docker-compose.yml` file under the `environment` section: `GEMINI_API_KEY=your_key_here`.
3. **Hardcoded (Local):** In `main.py`, replace line 43 (`api_key = request.api_key or os.getenv("GEMINI_API_KEY")`) with `api_key = "your_key_here"`.

## 🛠️ Technology Stack
- **Backend:** FastAPI, Python, PyPDF2
- **AI Model:** Google Gemini 3.5 Flash (`google-genai` SDK)
- **Frontend:** HTML5, JavaScript (Fetch API), Tailwind CSS

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
