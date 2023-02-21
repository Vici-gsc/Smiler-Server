from pydantic import BaseModel


class ImitationPhoto(BaseModel):
    feeling: str
    photo_url: str


class ImitationFace(BaseModel):
    match: bool
    recognize: str
