from django.conf import settings
from rest_framework.authentication import BaseAuthentication

from .exceptions import AuthenticationFailed
from .models import UserFactory
from .token import Token


class CustomJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        jwt_token = self.get_token(request)
        token = Token()

        data = token.get_token_data(jwt_token)
        if not data:
            raise AuthenticationFailed('No data')
        user_class = UserFactory().get_user(data.pop('role'))
        return user_class(**data), jwt_token

    def get_token(self, request) -> str:
        if settings.GET_TOKEN_FROM == 'headers':
            token = self._get_token_from_header(request)
        else:
            token = self._get_token_from_cookies(request)

        if not token:
            raise AuthenticationFailed('Token not found in %s' % settings.GET_TOKEN_FROM)
        return token

    @staticmethod
    def _get_token_from_header(request) -> str:
        token = request.META.get('HTTP_AUTHORIZATION')
        return token

    @staticmethod
    def _get_token_from_cookies(request) -> str:
        token = request.COOKIES.get('Authentication')
        return token
