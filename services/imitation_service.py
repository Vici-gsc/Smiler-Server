from sqlalchemy import func

from utils.app_exceptions import AppException
from utils.service_result import ServiceResult

from fastapi import UploadFile

from services.ai_model import FaceEmotionRecognition
from PIL import Image
from io import BytesIO

from services.main import AppService, AppCRUD
from config.emotion_url import UrlItem


class ImitationService(AppService):
    def get_photo_url(self, feeling: str) -> ServiceResult:
        photo_url = ImitationCRUD(self.db).get_photo_url(feeling)
        if not photo_url:
            return ServiceResult(AppException.CantGetPhotoFromGCP())

        return ServiceResult({"feeling": feeling, "photo_url": photo_url})

    def is_feeling_match(self, feeling: str, file: UploadFile) -> ServiceResult:
        if not file:
            return ServiceResult(AppException.ImageNotFound())

        # predict emotion using model
        img = Image.open(BytesIO(file.file.read()))
        pred = FaceEmotionRecognition()(img)
        if not pred:
            return ServiceResult(AppException.NoResultFromModel())

        # get expression is same or not same
        is_match = (pred == feeling)

        return ServiceResult({"match": is_match, "recognize": pred})


class ImitationCRUD(AppCRUD):
    def get_photo_url(self, feeling: str) -> str:
        query = self.db.query(UrlItem.url).filter_by(emotion=feeling).order_by(func.rand()).limit(1)
        url = query.scalar()

        return url
