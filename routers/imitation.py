from fastapi import APIRouter

router = APIRouter(
    prefix="/imitation",
    tags=["imitation"],
    responses={404: {"description": "Not found"}},
)
