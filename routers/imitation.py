from fastapi import APIRouter, UploadFile, Depends

from models.imitation import ImitationPhoto, ImitationFace

from utils.service_result import handle_result
from services.imitation_service import ImitationService

from config.database import get_db

router = APIRouter(
    prefix="/imitation",
    tags=["imitation"],
    responses={404: {"description": "Not found"}},
)


@router.get("/photo", response_model=ImitationPhoto)
async def get_photo(feeling: str, db: get_db = Depends()):
    result = ImitationService(db).get_photo_url(feeling)
    return handle_result(result)


@router.post("/face", response_model=ImitationFace)
async def is_feeling_match(feeling: str, file: UploadFile, db: get_db = Depends()):
    result = ImitationService(db).is_feeling_match(feeling, file)
    return handle_result(result)
