import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import PyPDF2
from google import genai

app = FastAPI(title="Active Reading API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return FileResponse("static/index.html")

@app.post("/api/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files supported.")
    try:
        reader = PyPDF2.PdfReader(file.file)
        text = "\n\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
        return {"filename": file.filename, "text": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class ChatRequest(BaseModel):
    document_text: str
    prompt: str
    api_key: str = None

@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    api_key = "Your API Key"
    if not api_key:
        raise HTTPException(status_code=401, detail="Missing Gemini API Key.")

    async def stream_generator():
        try:
            # Initialize the async client using the modern SDK
            client = genai.Client(api_key=api_key).aio
            
            combined_prompt = (
                "You are an expert AI Tutor. Use the provided document context to "
                "answer the user's question clearly and accurately.\n\n"
                f"DOCUMENT CONTEXT:\n{request.document_text[:50000]}\n\n" 
                f"USER QUESTION: {request.prompt}"
            )
            
            # Stream the response
            response = await client.models.generate_content_stream(
                model='gemini-3.5-flash',
                contents=combined_prompt
            )
            
            async for chunk in response:
                if chunk.text:
                    yield chunk.text
                    
        except Exception as e:
            yield f"\n\n[Error: {str(e)}]"

    return StreamingResponse(stream_generator(), media_type="text/plain")