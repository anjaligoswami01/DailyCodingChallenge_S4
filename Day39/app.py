from fastapi import FastAPI
from retrieval import retrieve_documents

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Day 39 AI Product Iteration"}


@app.get("/ask")
def ask(question: str):

    docs, retrieval_score = retrieve_documents(question)

    answer = f"Retrieved Context: {docs}"

    if retrieval_score < 0.4:
        answer += (
            "\n\n"
            "⚠️ Confidence is low.\n"
            "Is this answer helpful? Yes or No"
        )

    return {
        "answer": answer,
        "score": retrieval_score
    }