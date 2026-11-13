import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import google.generativeai as genai
from supabase import create_client, Client

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Supabase Setup
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
supabase: Client = None
if SUPABASE_URL and SUPABASE_KEY:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Google Gemini API Setup
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    # Using Gemini Flash model for fast & free responses
    model = genai.GenerativeModel("gemini-1.5-flash")

class ChatRequest(BaseModel):
    message: str
    language: str = "Telugu"
    mode: str = "local_info"
    session_id: str = "default-user"

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/admin", response_class=HTMLResponse)
async def admin_page(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    try:
        if not GEMINI_API_KEY:
            raise HTTPException(status_code=500, detail="Gemini API Key is missing in environment variables.")

        # Construct prompt based on mode and language
        system_prompt = f"""
        You are an AI assistant for the Vijayawada All-in-One Local Platform.
        Mode: {req.mode}
        Language: Please reply strictly in {req.language}.
        User Question: {req.message}
        """

        # Generate response from Gemini
        response = model.generate_content(system_prompt)
        reply_text = response.text if response and response.text else "సమాచారం అందలేదు."

        return {"reply": reply_text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
