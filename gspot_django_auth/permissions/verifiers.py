from ..models import CustomerUser, DeveloperUser, AdminUser, BaseUser


class AbstractUserVerify:
    """Common abstract class for user verification"""

    def verify(self, user: BaseUser) -> bool:
        """check user verification by condition"""
        raise NotImplementedError


class IsActiveUserVerify(AbstractUserVerify):
    def verify(self, user):
        return user.is_active


class NotBannedUserVerify(AbstractUserVerify):
    def verify(self, user):
        return not user.is_banned


class IsAdminSuperUserVerify(AbstractUserVerify):
    def verify(self, user):
        if isinstance(user, AdminUser):
            return user.is_superuser
        return False


class IsCompanySuperUserVerify(AbstractUserVerify):
    def verify(self, user):
        if isinstance(user, DeveloperUser):
            return user.is_superuser
        return False


class AdminScopeUserVerify(AbstractUserVerify):
    def verify(self, user) -> bool:
        return isinstance(user, AdminUser)


class CompanyScopeUserVerify(AbstractUserVerify):
    def verify(self, user) -> bool:
        return isinstance(user, DeveloperUser)


class CustomerScopeUserVerify(AbstractUserVerify):
    def verify(self, user) -> bool:
        return isinstance(user, CustomerUser)


class CompanyOwnerVerify(AbstractUserVerify):
    def verify(self, user) -> bool:
        if isinstance(user, DeveloperUser):
            return user.is_superuser
        return False


class CompanyEmployeeVerify(AbstractUserVerify):
    def verify(self, user):
        if isinstance(user, DeveloperUser):
            if user.company:
                return user.company.get('created_by') != user
        return False
