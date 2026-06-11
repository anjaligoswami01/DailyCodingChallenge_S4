from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Backend")

# Allow requests from your Vercel frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://your-app.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "status": "healthy",
        "message": "AI Backend Running"
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
async def chat(request: dict):
    query = request.get("query", "")

    # Replace with your actual AI logic
    response = f"You asked: {query}"

    return {
        "answer": response,
        "sources": []
    }