from fastapi import APIRouter, Depends

from models.word import WordItem

from utils.service_result import handle_result
from services.word_service import WordService

from config.database import get_db

router = APIRouter(
    prefix="/word",
    tags=["word"],
    responses={404: {"description": "Not found"}},
)

@router.get("", response_model=WordItem)
async def get_photo(db: get_db = Depends()):
    result = WordService(db).get_word_info()
    return handle_result(result)
