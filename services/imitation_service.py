from utils.app_exceptions import AppException
from utils.service_result import ServiceResult


class ImitationService:
    def get_photo_url(self, feeling: str) -> ServiceResult:
        photo_url = ImitationCRUD().get_photo_url(feeling)
        if not photo_url:
            return ServiceResult(AppException.ImitationGetPhoto())

        return ServiceResult({"feeling": feeling, "photo_url": photo_url})


class ImitationCRUD:
    def get_photo_url(self, feeling: str) -> str:
        # get photo_url from google cloud platform
        return "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.google.co.jp%2F%3Fhl%3Dko&psig=AOvVaw0dqHXQLluo0GuLbTbcAvhp&ust=1676904308339000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCLCBmb_pof0CFQAAAAAdAAAAABAD"
