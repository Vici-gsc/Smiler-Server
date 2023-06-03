from src.utils.app_exceptions import AppException
from src.utils.service_result import ServiceResult

from fastapi import UploadFile
from src.services.ai_model import FaceEmotionRecognition

from PIL import Image
from io import BytesIO


class ExpressionService:
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
