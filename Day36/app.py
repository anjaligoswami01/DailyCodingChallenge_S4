from fastapi import FastAPI
import os

app = FastAPI()

MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4")
SIMILARITY_THRESHOLD = float(
    os.getenv("SIMILARITY_THRESHOLD", "0.75")
)

@app.get("/")
def root():
    return {
        "message": "AI Backend Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.post("/query")
def query(payload: dict):
    question = payload.get("question")

    return {
        "question": question,
        "model": MODEL_NAME,
        "threshold": SIMILARITY_THRESHOLD,
        "answer": f"Processed: {question}"
    }