from fastapi import APIRouter, UploadFile

from models.imitation import ImitationPhoto, ImitationFace

from utils.service_result import handle_result
from services.imitation_service import ImitationService

router = APIRouter(
    prefix="/imitation",
    tags=["imitation"],
    responses={404: {"description": "Not found"}},
)


@router.get("/photo", response_model=ImitationPhoto)
async def get_photo(feeling: str):
    result = ImitationService().get_photo_url(feeling)
    return handle_result(result)


@router.post("/face", response_model=ImitationFace)
async def is_feeling_match(file: UploadFile):
    result = ImitationService().is_feeling_match(file)
    return handle_result(result)
