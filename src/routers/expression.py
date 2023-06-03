from fastapi import APIRouter, UploadFile

from src.models.expression import ExpressionItem

from src.utils.service_result import handle_result
from src.services.expression_service import ExpressionService

router = APIRouter(
    prefix="/expression",
    tags=["expression"],
    responses={404: {"description": "Not found"}},
)


@router.post("", response_model=ExpressionItem)
async def is_feeling_match(feeling: str, file: UploadFile):
    result = ExpressionService().is_feeling_match(feeling, file)
    return handle_result(result)
