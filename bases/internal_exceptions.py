from rest_framework.exceptions import APIException


class DuplicatedBackGroundFieldPerUser(APIException):
    status_code = 400
    default_code = 1000
    default_detail = "already  background field exists for current user"
