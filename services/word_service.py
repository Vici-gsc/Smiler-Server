from sqlalchemy import func

import random

from utils.app_exceptions import AppException
from utils.service_result import ServiceResult
from utils.feelings import feelings

from services.main import AppService, AppCRUD
from config.emotion_url import UrlItem


class WordService(AppService):
    def get_word_info(self) -> ServiceResult:
        feeling_list = random.sample(feelings, 5)
        feeling = random.sample(feeling_list, 1)[0]

        photo_url = WordCRUD(self.db).get_photo_url(feeling)
        if not photo_url:
            return ServiceResult(AppException.CantGetPhotoFromGCP())

        return ServiceResult({"answer": feeling, "feeling_list": feeling_list, "photo_url": photo_url})


class WordCRUD(AppCRUD):
    def get_photo_url(self, feeling: str) -> str:
        # get photo_url from google cloud platform
        query = self.db.query(UrlItem.url).filter_by(emotion=feeling).order_by(func.rand()).limit(1)
        url = query.scalar()
        return url
