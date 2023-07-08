from .redis_client import RedisAccessClient


class Token:
    redis_client: RedisAccessClient = RedisAccessClient()

    def get_token_data(self, token: str) -> dict:
        data = self.redis_client.is_token_exist(token)
        return data
