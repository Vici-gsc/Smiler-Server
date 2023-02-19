from fastapi import APIRouter

from models.imitation import ImitationPhoto

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
