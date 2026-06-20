from pydantic import BaseModel


class AskRequest(BaseModel):
    session_id: str
    query: str


class FeedbackRequest(BaseModel):
    session_id: str
    query: str
    rating: int
    helpful: bool
    comments: str


class AskResponse(BaseModel):
    response: str


class ErrorResponse(BaseModel):
    error: str