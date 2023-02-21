from fastapi import APIRouter

from models.word import WordItem

from utils.service_result import handle_result
from services.word_service import WordService


router = APIRouter(
    prefix="/word",
    tags=["word"],
    responses={404: {"description": "Not found"}},
)

@router.get("", response_model=WordItem)
async def get_photo():
    result = WordService().get_word_info()
    return handle_result(result)
