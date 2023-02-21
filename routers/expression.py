from fastapi import APIRouter, UploadFile

from models.expression import ExpressionItem

from utils.service_result import handle_result
from services.expression_service import ExpressionService

router = APIRouter(
    prefix="/expression",
    tags=["expression"],
    responses={404: {"description": "Not found"}},
)


@router.post("", response_model=ExpressionItem)
async def is_feeling_match(file: UploadFile):
    result = ExpressionService().is_feeling_match(file)
    return handle_result(result)
