from utils.app_exceptions import AppExceptionCase, app_exception_handler
from fastapi import FastAPI

from routers import imitation, word, expression

app = FastAPI()


@app.exception_handler(AppExceptionCase)
async def custom_app_exception_handler(request, e):
    return await app_exception_handler(request, e)


app.include_router(imitation.router)
app.include_router(word.router)
app.include_router(expression.router)
