from pydantic import BaseModel

class AskRequest(BaseModel):
    query: str

class AskResponse(BaseModel):
    response: str

class ErrorResponse(BaseModel):
    error: str