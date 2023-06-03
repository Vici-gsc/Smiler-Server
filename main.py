from src.utils.app_exceptions import AppExceptionCase, app_exception_handler
from fastapi import FastAPI

from src.routers import imitation, word, expression
from src.services.ai_model import FaceEmotionRecognition

app = FastAPI()
FaceEmotionRecognition()


@app.exception_handler(AppExceptionCase)
async def custom_app_exception_handler(request, e):
    return await app_exception_handler(request, e)


app.include_router(imitation.router)
app.include_router(word.router)
app.include_router(expression.router)
