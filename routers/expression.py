from fastapi import APIRouter

router = APIRouter(
    prefix="/expression",
    tags=["expression"],
    responses={404: {"description": "Not found"}},
)
