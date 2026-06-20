from fastapi import FastAPI
from fastapi import HTTPException

from models import AskRequest
from core_ai import core_ai_loop

app = FastAPI(
    title="AI Data Engineering Mentor MVP"
)

@app.post("/ask")
def ask_question(request: AskRequest):

    try:

        answer = core_ai_loop(
            request.query
        )

        return {
            "response": answer
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail={
                "error": str(e)
            }
        )