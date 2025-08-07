from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from gemini_backend import get_response_from_gemini
from fastapi.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatInput(BaseModel):
    message: str

@app.get("/")
def get_index():
    return FileResponse("index.html")

@app.post("/chat")
async def chat(input_data: ChatInput):
    reply = get_response_from_gemini(input_data.message)
    return {"reply": reply}

