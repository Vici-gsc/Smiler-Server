from utils.app_exceptions import AppException
from utils.service_result import ServiceResult

from fastapi import UploadFile

from services.ai_model import FaceEmotionRecognition
from PIL import Image
from io import BytesIO


class ImitationService:
    def get_photo_url(self, feeling: str) -> ServiceResult:
        photo_url = ImitationCRUD().get_photo_url(feeling)
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


class ImitationCRUD:
    def get_photo_url(self, feeling: str) -> str:
        # get photo_url from google cloud platform
        return "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.google.co.jp%2F%3Fhl%3Dko&psig=AOvVaw0dqHXQLluo0GuLbTbcAvhp&ust=1676904308339000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCLCBmb_pof0CFQAAAAAdAAAAABAD"
