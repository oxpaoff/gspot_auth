import jwt
from django.conf import settings
from jwt.exceptions import ExpiredSignatureError

from exceptions import TokenInvalid, TokenExpired
from .redis_client import RedisAccessClient


class Token:
    redis_client: RedisAccessClient = RedisAccessClient()

    @staticmethod
    def _decode(token: str) -> dict:
        try:
            return jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
        except ExpiredSignatureError:
            raise TokenExpired('Token is expired')
        except Exception:
            raise TokenInvalid("%s is invalid token" % token)

    def get_token_data(self, token: str) -> dict:
        data = self.redis_client.is_token_exist(token)
        return data
