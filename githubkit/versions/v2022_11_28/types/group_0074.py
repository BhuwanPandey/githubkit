"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict, NotRequired


class TeamSimpleType(TypedDict):
    """Team Simple

    Groups of organization members that gives permissions on specified repositories.
    """

    id: int
    node_id: str
    url: str
    members_url: str
    name: str
    description: Union[str, None]
    permission: str
    privacy: NotRequired[str]
    notification_setting: NotRequired[str]
    html_url: str
    repositories_url: str
    slug: str
    ldap_dn: NotRequired[str]


__all__ = ("TeamSimpleType",)
