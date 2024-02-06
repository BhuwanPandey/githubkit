"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType


class OrgMembershipType(TypedDict):
    """Org Membership

    Org Membership
    """

    url: str
    state: Literal["active", "pending"]
    role: Literal["admin", "member", "billing_manager"]
    organization_url: str
    organization: OrganizationSimpleType
    user: Union[None, SimpleUserType]
    permissions: NotRequired[OrgMembershipPropPermissionsType]


class OrganizationSimpleType(TypedDict):
    """Organization Simple

    A GitHub organization.
    """

    login: str
    id: int
    node_id: str
    url: str
    repos_url: str
    events_url: str
    hooks_url: str
    issues_url: str
    members_url: str
    public_members_url: str
    avatar_url: str
    description: Union[str, None]


class OrgMembershipPropPermissionsType(TypedDict):
    """OrgMembershipPropPermissions"""

    can_create_repository: bool


__all__ = (
    "OrgMembershipType",
    "OrganizationSimpleType",
    "OrgMembershipPropPermissionsType",
)
