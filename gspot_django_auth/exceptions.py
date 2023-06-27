from rest_framework.exceptions import APIException
from rest_framework import status


class AuthenticationFailed(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED


class NoPermission(APIException):
    status_code = status.HTTP_403_FORBIDDEN


class TokenExpired(AuthenticationFailed):
    pass


class TokenInvalid(AuthenticationFailed):
    pass
