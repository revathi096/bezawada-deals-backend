import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import google.generativeai as genai

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Safe Google Gemini API Setup (Doesn't crash if key is missing)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "dummy-key")
if GEMINI_API_KEY and GEMINI_API_KEY != "dummy-key":
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    model = None

class ChatRequest(BaseModel):
    message: str
    language: str = "Telugu"
    mode: str = "local_info"
    session_id: str = "default-user"

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    try:
        if not model:
            return {"reply": "జెమిని ఏఐ కీ (Gemini API Key) సెట్ చేయబడలేదు. దయచేసి రెండర్‌లో కీ జోడించండి."}
        
        system_prompt = f"""
        You are an AI assistant for the Vijayawada Smart Needs Platform.
        Mode: {req.mode}
        Language: Please reply strictly in {req.language}.
        User Question: {req.message}
        """
        response = model.generate_content(system_prompt)
        reply_text = response.text if response and response.text else "సమాచారం అందలేదు."
        return {"reply": reply_text}
    except Exception as e:
        return {"reply": f"సమస్య ఏర్పడింది: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)
