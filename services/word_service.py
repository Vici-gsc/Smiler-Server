import random

from utils.app_exceptions import AppException
from utils.service_result import ServiceResult
from utils.feelings import feelings


class WordService:
    def get_word_info(self) -> ServiceResult:
        feeling_list = random.sample(feelings, 5)
        feeling = random.sample(feeling_list, 1)[0]

        photo_url = WordCRUD().get_photo_url(feeling)
        if not photo_url:
            return ServiceResult(AppException.CantGetPhotoFromGCP())

        return ServiceResult({"answer": feeling, "feeling_list": feeling_list, "photo_url": photo_url})


class WordCRUD:
    def get_photo_url(self, feeling: str) -> str:
        # get photo_url from google cloud platform
        return "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.google.co.jp%2F%3Fhl%3Dko&psig=AOvVaw0dqHXQLluo0GuLbTbcAvhp&ust=1676904308339000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCLCBmb_pof0CFQAAAAAdAAAAABAD"
