import json

import redis
from django.conf import settings


class RedisAccessClient:
    _prefix = settings.REDIS_ACCESS_PREFIX

    def __init__(self):
        db = settings.REDIS_ACCESS_DB
        host = settings.REDIS_HOST
        port = settings.REDIS_PORT
        password = settings.REDIS_PASSWORD
        self.__redis_client = redis.StrictRedis(host=host, port=port, db=db, password=password)

    @property
    def conn(self):
        return self.__redis_client

    def __get(self, name: str) -> dict | None:
        value = self.conn.get(name)
        if value:
            return json.loads(value)

    def __put(self, name: str, value: dict, ttl: int) -> None:
        value_data = json.dumps(value)
        self.conn.set(name=name, value=value_data, ex=ttl)

    def is_token_exist(self, token: str, prefix: bool = True) -> dict | None:
        key = f'{self._prefix}:{token}' if prefix else token
        return self.__get(key)
