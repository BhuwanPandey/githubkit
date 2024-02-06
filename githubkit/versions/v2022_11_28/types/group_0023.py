"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0021 import SimpleClassroomRepositoryType


class ClassroomAcceptedAssignmentType(TypedDict):
    """Classroom Accepted Assignment

    A GitHub Classroom accepted assignment
    """

    id: int
    submitted: bool
    passing: bool
    commit_count: int
    grade: str
    students: List[SimpleClassroomUserType]
    repository: SimpleClassroomRepositoryType
    assignment: SimpleClassroomAssignmentType


class SimpleClassroomUserType(TypedDict):
    """Simple Classroom User

    A GitHub user simplified for Classroom.
    """

    id: int
    login: str
    avatar_url: str
    html_url: str


class SimpleClassroomAssignmentType(TypedDict):
    """Simple Classroom Assignment

    A GitHub Classroom assignment
    """

    id: int
    public_repo: bool
    title: str
    type: Literal["individual", "group"]
    invite_link: str
    invitations_enabled: bool
    slug: str
    students_are_repo_admins: bool
    feedback_pull_requests_enabled: bool
    max_teams: NotRequired[Union[int, None]]
    max_members: NotRequired[Union[int, None]]
    editor: str
    accepted: int
    submitted: int
    passing: int
    language: str
    deadline: Union[datetime, None]
    classroom: SimpleClassroomType


class SimpleClassroomType(TypedDict):
    """Simple Classroom

    A GitHub Classroom classroom
    """

    id: int
    name: str
    archived: bool
    url: str


__all__ = (
    "ClassroomAcceptedAssignmentType",
    "SimpleClassroomUserType",
    "SimpleClassroomAssignmentType",
    "SimpleClassroomType",
)
