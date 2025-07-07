
from fastapi import APIRouter
from pydantic import BaseModel
from services.chatbot_service import get_chatbot_response

router = APIRouter()

class ChatQuery(BaseModel):
    question: str
    language: str = "en"

@router.post("/")
async def ask_chatbot(query: ChatQuery):
    answer = get_chatbot_response(query.question, query.language)
    return {"answer": answer}
