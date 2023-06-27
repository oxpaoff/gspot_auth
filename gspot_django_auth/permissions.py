from .exceptions import NoPermission

from .models import AdminUser, CustomerUser, DeveloperUser


def is_customer(user: CustomerUser):
    if isinstance(user, CustomerUser):
        return user
    else:
        raise NoPermission()


def is_admin(user: AdminUser):
    if isinstance(user, AdminUser):
        return user
    else:
        raise NoPermission()


def is_developer(user: DeveloperUser):
    if isinstance(user, DeveloperUser):
        return user
    else:
        raise NoPermission()


__all__ = ['is_developer', 'is_customer', 'is_admin']