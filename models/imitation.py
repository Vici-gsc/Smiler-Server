from pydantic import BaseModel


class ImitationPhoto(BaseModel):
    feeling: str
    photo_url: str

