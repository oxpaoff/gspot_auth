from rest_framework.permissions import BasePermission

from . import verifiers


class BaseUserPermissions(verifiers.AbstractUserVerify, BasePermission):
    def has_permission(self, request, view):
        return self.verify(request.user)


class IsAdminSuperUserPerm(BaseUserPermissions, verifiers.IsAdminSuperUserVerify):
    """Check Admin Super User Permission"""


class IsCompanySuperUserPerm(BaseUserPermissions, verifiers.IsCompanySuperUserVerify):
    """Check Admin Super User Permission"""


class IsAdminScopeUserPerm(BaseUserPermissions, verifiers.AdminScopeUserVerify):
    """Check Admin User"""


class IsCompanyScopeUserPerm(BaseUserPermissions, verifiers.CompanyScopeUserVerify):
    """Check Company User"""


class IsCustomerScopeUserPerm(BaseUserPermissions, verifiers.CustomerScopeUserVerify):
    """Check Customer User"""


class CompanyOwnerPerm(BaseUserPermissions, verifiers.CompanyOwnerVerify):
    """Check Company Owner"""


class CompanyEmployeePerm(BaseUserPermissions, verifiers.CompanyEmployeeVerify):
    """Check Company Employee"""
