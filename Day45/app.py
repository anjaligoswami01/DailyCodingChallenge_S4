import uuid
import time

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Depends

from models import AskRequest
from models import FeedbackRequest

from core_ai import core_ai_loop

from database import conn
from database import cursor

from auth import verify_api_key
from rate_limiter import check_rate_limit

app = FastAPI(
    title="AI Data Engineering Mentor MVP"
)

# Session Storage
sessions = {}


@app.get("/history/{session_id}")
def get_history(
    session_id: str,
    api_key: str = Depends(
        verify_api_key
    )
):

    return {
        "messages": sessions.get(session_id, [])
    }


@app.post("/session/create")
def create_session(
    api_key: str = Depends(
        verify_api_key
    )
):

    session_id = str(uuid.uuid4())

    sessions[session_id] = []

    return {
        "session_id": session_id
    }


@app.post("/ask")
def ask_question(
    request: AskRequest,
    api_key: str = Depends(
        verify_api_key
    )
):

    try:

        if not check_rate_limit(
            request.session_id
        ):

            raise HTTPException(
                status_code=429,
                detail="You have reached the limit of 20 requests per hour."
            )

        start_time = time.time()

        answer = core_ai_loop(
            request.query
        )

        latency_ms = int(
            (time.time() - start_time) * 1000
        )

        retrieval_score = 0.90

        sessions.setdefault(
            request.session_id,
            []
        )

        sessions[request.session_id].append(
            {
                "user": request.query,
                "assistant": answer
            }
        )

        cursor.execute(
            """
            INSERT INTO logs (
                session_id,
                query,
                response_excerpt,
                latency_ms,
                retrieval_score
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                request.session_id,
                request.query,
                answer[:100],
                latency_ms,
                retrieval_score
            )
        )

        conn.commit()

        return {
            "response": answer,
            "latency_ms": latency_ms,
            "retrieval_score": retrieval_score
        }

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail={
                "error": str(e)
            }
        )


@app.post("/feedback")
def submit_feedback(
    request: FeedbackRequest,
    api_key: str = Depends(
        verify_api_key
    )
):

    cursor.execute(
        """
        INSERT INTO feedback (
            session_id,
            query,
            rating,
            helpful,
            comments
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            request.session_id,
            request.query,
            request.rating,
            request.helpful,
            request.comments
        )
    )

    conn.commit()

    return {
        "status": "saved"
    }