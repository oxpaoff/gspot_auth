import json

from django.core.management import BaseCommand

from gspot_django_auth.redis_client import RedisAccessClient


class Command(BaseCommand):
    def handle(self, *args, **options):
        tokens = self.get_tokens()
        self.add_to_redis(tokens)

    @staticmethod
    def get_tokens() -> dict:
        admin_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiaWF0IjoxNjg5NjgyNzczLCJleHAiOjE2ODk2ODMwNzN9.Q-_Lz4GmjTJuprbsKv4jSW3OGZ-ixxCmRGHva8KLkoM"
        admin_data = {
            "username": "admin_username",
            "first_name": "admin_first_name",
            "last_name": "admin_last_name",
            "is_banned": False,
            "is_active": True,
            "user_id": "7fff5488-a091-44a1-9a4e-cb9f535a7f34",
            "role": "administrator",
            "avatar": "",
            "permissions": [],
            "email": "admin@gmail.com",
            "phone": "88005553535",
            "country": None,
            "created_at": "2023-07-08 21:04:32.226941+00:00",
            "update_at": "2023-07-08 21:04:32.226953+00:00",
            "is_superuser": False,
            "groups": [],
            "user_permissions": [],
            "developer_groups": [],
            "developer_permissions": []
        }
        admin_superuser_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiaWF0IjoxNjg5NjgyNzcwLCJleHAiOjE2ODk2ODMwODB9.47CONTJjEqoL6JMjyERM5WJYYA5jna55w6CXaoW55PI"
        admin_superuser_data = {
            "username": "admin_username",
            "first_name": "admin_first_name",
            "last_name": "admin_last_name",
            "is_banned": False,
            "is_active": True,
            "user_id": "7fff5488-a091-44a1-9a4e-cb9f535a7f34",
            "role": "administrator",
            "avatar": "",
            "permissions": [],
            "email": "admin@gmail.com",
            "phone": "88005553535",
            "country": None,
            "created_at": "2023-07-08 21:04:32.226941+00:00",
            "update_at": "2023-07-08 21:04:32.226953+00:00",
            "is_superuser": True,
            "groups": [],
            "user_permissions": [],
            "developer_groups": [],
            "developer_permissions": []
        }

        dev_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiaWF0IjoxNjg5NjgzMTI3LCJleHAiOjE2ODk2ODM0Mjd9.h-pqm9eDO9yOs2FrHIW0nPTwT45kT9rHvieYfvJoUXc"
        dev_data = {
            "username": "dev_username",
            "first_name": "dev_first_name",
            "last_name": "dev_last_name",
            "is_banned": False,
            "user_id": "9c490b97-4423-4fae-8beb-7e0a128f469f",
            "role": "developer",
            "avatar": "",
            "permissions": [],
            "email": "developer@gmail.com",
            "phone": "88005553535",
            "country": {
                "id": 1,
                "name": "Russia"
            },
            "created_at": "2023-07-18 12:15:50.005936+00:00",
            "update_at": "2023-07-18 12:18:50.540200+00:00",
            "is_active": True,
            "is_superuser": False,
            "groups": [],
            "user_permissions": [],
            "company": {}
        }
        owner_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiaWF0IjoxNjg5NjgzNTQwLCJleHAiOjE2ODk2ODM4NDB9.o8QLclmTxUOEUiVlvHyEghdjtKRbEYn9eAk_jXCswhQ"
        owner_data = {
            "username": "owner_username",
            "first_name": "owner_first_name",
            "last_name": "owner_last_name",
            "is_banned": False,
            "user_id": "36041f78-e46a-4c62-81a6-c0c9e7cce5a4",
            "role": "developer",
            "avatar": "",
            "permissions": [],
            "email": "company_owner@gmail.com",
            "phone": "88005553535",
            "country": {
                "id": 1,
                "name": "Russia"
            },
            "created_at": "2023-07-18 12:30:50.413011+00:00",
            "update_at": "2023-07-18 12:32:17.309680+00:00",
            "is_active": True,
            "is_superuser": False,
            "groups": [],
            "user_permissions": [],
            "company": {
                "created_by": "9c490b97-4423-4fae-8beb-7e0a128f469f",
                "title": "Test Company",
                "description": "Test Company Description",
                "email": "test_company@gmail.com",
                "image": "",
                "is_confirmed": True,
                "is_active": True,
                "is_banned": False,
                "contact": []
            }
        }
        customer_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiaWF0IjoxNjg5Njg0MDMxLCJleHAiOjE2ODk2ODQzMzF9.07kcY4cQWmw20PMf9NWrvxR7NbuVIoCmlN2Gi-hIi7A"
        customer_data = {
            "username": "customer_username",
            "first_name": "customer_first_name",
            "last_name": "customer_last_name",
            "is_banned": False,
            "user_id": "fd3e3c48-96fc-4863-9aa8-68d1e43a6750",
            "role": "customer",
            "avatar": "",
            "permissions": [],
            "age": 18,
            "email": "customer@gmail.com",
            "phone": "88005553535",
            "created_at": "2023-07-18 12:36:56.545791+00:00",
            "update_at": "2023-07-18 12:37:13.736690+00:00",
            "friends": ["dcada25f-b104-4b12-8ac1-9364252b9e7d"],
            "birthday": "2023-07-18",
            "is_active": True,
            "country": {
                "id": 1,
                "name": "Russia"
            }
        }
        tokens = {
            admin_token: admin_data,
            admin_superuser_token: admin_superuser_data,
            dev_token: dev_data,
            owner_token: owner_data,
            customer_token: customer_data
        }
        return tokens

    @staticmethod
    def add_to_redis(tokens: dict):
        redis_client = RedisAccessClient()
        for token, value in tokens.items():
            name = f'{redis_client._prefix}:{token}'
            try:
                redis_client.conn.delete(name)
            except:
                pass
            value_data = json.dumps(value)
            redis_client.conn.set(name=name, value=value_data)
