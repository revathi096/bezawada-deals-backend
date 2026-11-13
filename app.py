
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="My Advanced AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):

    response = client.responses.create(
        model="gpt-6",
        instructions="""
        You are an intelligent multilingual AI assistant.
        Answer in Telugu or English based on the user's language.
        Give accurate, clear and useful answers.
        """,
        input=request.message
    )

    return {
        "answer": response.output_text
    }

@app.get("/")
def home():
    return {"status": "AI is running"}
