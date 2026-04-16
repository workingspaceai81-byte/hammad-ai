from fastapi import FastAPI
import ollama

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()

# CORS Fix
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home Page (HTML load karega)
@app.get("/")
def home():
    return FileResponse("web/index.html")


# Chat API
@app.get("/chat")
def chat(msg: str):
    response = ollama.chat(
        model="gemma4:e2b",
        messages=[
            {"role": "user", "content": msg}
        ]
    )
    return {"response": response["message"]["content"]}