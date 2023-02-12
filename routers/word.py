from fastapi import APIRouter

router = APIRouter(
    prefix="/word",
    tags=["word"],
    responses={404: {"description": "Not found"}},
)
