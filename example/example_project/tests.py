from django.conf import settings
from unittest.mock import patch
from rest_framework.test import APIClient
from django.test import TestCase

from gspot_django_auth.redis_client import RedisAccessClient
from .factory import AdminUserFactory, CustomerUserFactory, DeveloperUserFactory


class TestRedisService(TestCase):

    def setUp(self) -> None:
        self.redis = RedisAccessClient()
        self.client = APIClient()
        self.url = '/'

    @patch('gspot_django_auth.token.Token.get_token_data')
    def test_auth_admin_valid_from_headers(self, redis_mock):
        settings.GET_TOKEN_FROM = 'headers'
        user_data = AdminUserFactory().to_dict()
        user_data['role'] = 'administrator'
        redis_mock.return_value = user_data

        headers = {'Authorization': 'token'}
        response = self.client.get(self.url, headers=headers)
        self.assertEqual(response.status_code, 200)

    @patch('gspot_django_auth.token.Token.get_token_data')
    def test_auth_developer_valid_from_headers(self, redis_mock):
        settings.GET_TOKEN_FROM = 'headers'
        user_data = DeveloperUserFactory().to_dict()
        user_data['role'] = 'developer'
        redis_mock.return_value = user_data

        headers = {'Authorization': 'token'}
        response = self.client.get(self.url, headers=headers)
        self.assertEqual(response.status_code, 200)

    @patch('gspot_django_auth.token.Token.get_token_data')
    def test_auth_customer_valid_from_headers(self, redis_mock):
        settings.GET_TOKEN_FROM = 'headers'
        user_data = CustomerUserFactory().to_dict()
        user_data['role'] = 'customer'
        redis_mock.return_value = user_data

        headers = {'Authorization': 'token'}
        response = self.client.get(self.url, headers=headers)
        self.assertEqual(response.status_code, 200)

    @patch('gspot_django_auth.token.Token.get_token_data')
    def test_auth_admin_valid_from_cookies(self, redis_mock):
        settings.GET_TOKEN_FROM = 'cookies'
        user_data = AdminUserFactory().to_dict()
        user_data['role'] = 'administrator'
        redis_mock.return_value = user_data

        cookies = {'Authentication': 'token'}
        self.client.cookies.load(cookies)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    @patch('gspot_django_auth.token.Token.get_token_data')
    def test_auth_developer_valid_from_cookies(self, redis_mock):
        settings.GET_TOKEN_FROM = 'cookies'
        user_data = DeveloperUserFactory().to_dict()
        user_data['role'] = 'developer'
        redis_mock.return_value = user_data

        cookies = {'Authentication': 'token'}
        self.client.cookies.load(cookies)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    @patch('gspot_django_auth.token.Token.get_token_data')
    def test_auth_customer_valid_from_cookies(self, redis_mock):
        settings.GET_TOKEN_FROM = 'cookies'
        user_data = CustomerUserFactory().to_dict()
        user_data['role'] = 'customer'
        redis_mock.return_value = user_data

        cookies = {'Authentication': 'token'}
        self.client.cookies.load(cookies)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    @patch('gspot_django_auth.token.Token.get_token_data')
    def test_auth_customer_no_token_from_headers(self, redis_mock):
        settings.GET_TOKEN_FROM = 'headers'
        user_data = CustomerUserFactory().to_dict()
        user_data['role'] = 'customer'
        redis_mock.return_value = user_data

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)

    @patch('gspot_django_auth.token.Token.get_token_data')
    def test_auth_admin_no_token_from_cookies(self, redis_mock):
        settings.GET_TOKEN_FROM = 'cookies'
        user_data = AdminUserFactory().to_dict()
        user_data['role'] = 'administrator'
        redis_mock.return_value = user_data

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)

    @patch('gspot_django_auth.token.Token.get_token_data')
    def test_auth_customer_no_data_from_headers(self, redis_mock):
        settings.GET_TOKEN_FROM = 'headers'
        redis_mock.return_value = {}

        headers = {'Authorization': 'token'}
        response = self.client.get(self.url, headers=headers)
        self.assertEqual(response.status_code, 401)

    @patch('gspot_django_auth.token.Token.get_token_data')
    def test_auth_admin_no_data_from_cookies(self, redis_mock):
        settings.GET_TOKEN_FROM = 'cookies'
        redis_mock.return_value = {}

        cookies = {'Authentication': 'token'}
        self.client.cookies.load(cookies)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)
