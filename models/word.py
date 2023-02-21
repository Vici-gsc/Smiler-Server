from typing import List

from pydantic import BaseModel


class WordItem(BaseModel):
    answer: str
    feeling_list: List[str]
    photo_url: str
