from sqlalchemy import Column, Integer, String

from src.config.database import Base


class UrlItem(Base):
    __tablename__ = "emotion_url"

    id = Column(Integer, primary_key=True, index=True)
    emotion = Column(String)
    url = Column(String)
