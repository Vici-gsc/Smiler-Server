from pydantic import BaseModel


class ExpressionItem(BaseModel):
    match: bool
    recognize: str
