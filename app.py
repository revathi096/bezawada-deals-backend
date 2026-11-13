import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import google.generativeai as genai

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Gemini Setup
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    model = None

class ChatRequest(BaseModel):
    message: str
    language: str = "Telugu"
    mode: str = "local_info"

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # Safe template rendering
    return templates.TemplateResponse(request, "index.html", context={"request": request})

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    try:
        if not model:
            return {"reply": "API Key missing"}
        response = model.generate_content(f"Mode: {req.mode}. Reply in {req.language}: {req.message}")
        return {"reply": response.text if response and response.text else "No response"}
    except Exception as e:
        return {"reply": f"Error: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)
