"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict, NotRequired


class ExternalGroupType(TypedDict):
    """ExternalGroup

    Information about an external group's usage and its members
    """

    group_id: int
    group_name: str
    updated_at: NotRequired[str]
    teams: List[ExternalGroupPropTeamsItemsType]
    members: List[ExternalGroupPropMembersItemsType]


class ExternalGroupPropTeamsItemsType(TypedDict):
    """ExternalGroupPropTeamsItems"""

    team_id: int
    team_name: str


class ExternalGroupPropMembersItemsType(TypedDict):
    """ExternalGroupPropMembersItems"""

    member_id: int
    member_login: str
    member_name: NotRequired[Union[str, None]]
    member_email: str


__all__ = (
    "ExternalGroupType",
    "ExternalGroupPropTeamsItemsType",
    "ExternalGroupPropMembersItemsType",
)
