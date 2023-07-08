from abc import ABCMeta

from rest_framework.exceptions import ValidationError

from .verifiers import AbstractUserVerify, IsActiveUserVerify, NotBannedUserVerify
from ..models import BaseUser


class AbstractUserValidation(AbstractUserVerify, metaclass=ABCMeta):
    """Common abstract class for user validation"""

    exception: ValidationError

    def validate(self, user: BaseUser):
        """Raise error if user has not passed verification"""
        raise NotImplementedError


class BaseUserValidation(AbstractUserValidation):
    exception = ValidationError
    error_message = 'ValidationError'

    def __init__(self, message=''):
        if message:
            self.error_message = message

    def verify(self, user: BaseUser) -> bool:
        raise NotImplementedError

    def validate(self, user):
        if not self.verify(user):
            raise self.exception(self.error_message)


class ActiveUserValidator(IsActiveUserVerify, BaseUserValidation):
    """User Active Verification"""


class BannedUserValidatorVerify(NotBannedUserVerify, BaseUserValidation):
    """Banned User Verification"""
