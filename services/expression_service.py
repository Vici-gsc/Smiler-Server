from utils.app_exceptions import AppException
from utils.service_result import ServiceResult

from fastapi import UploadFile


class ExpressionService:
    def is_feeling_match(self, file: UploadFile) -> ServiceResult:
        if not file:
            return ServiceResult(AppException.ImageNotFound())

        # is_match, recognize = model.get ~~
        is_match = True
        recognize = "Happy"
        if not is_match or not recognize:
            return ServiceResult(AppException.NoResultFromModel())

        return ServiceResult({"match": is_match, "recognize": recognize})
