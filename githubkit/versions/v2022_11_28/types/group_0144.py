"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType
from .group_0016 import LicenseSimpleType


class TeamRepositoryType(TypedDict):
    """Team Repository

    A team's access to a repository.
    """

    id: int
    node_id: str
    name: str
    full_name: str
    license_: Union[None, LicenseSimpleType]
    forks: int
    permissions: NotRequired[TeamRepositoryPropPermissionsType]
    role_name: NotRequired[str]
    owner: Union[None, SimpleUserType]
    private: bool
    html_url: str
    description: Union[str, None]
    fork: bool
    url: str
    archive_url: str
    assignees_url: str
    blobs_url: str
    branches_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    deployments_url: str
    downloads_url: str
    events_url: str
    forks_url: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    languages_url: str
    merges_url: str
    milestones_url: str
    notifications_url: str
    pulls_url: str
    releases_url: str
    ssh_url: str
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    tags_url: str
    teams_url: str
    trees_url: str
    clone_url: str
    mirror_url: Union[str, None]
    hooks_url: str
    svn_url: str
    homepage: Union[str, None]
    language: Union[str, None]
    forks_count: int
    stargazers_count: int
    watchers_count: int
    size: int
    default_branch: str
    open_issues_count: int
    is_template: NotRequired[bool]
    topics: NotRequired[List[str]]
    has_issues: bool
    has_projects: bool
    has_wiki: bool
    has_pages: bool
    has_downloads: bool
    archived: bool
    disabled: bool
    visibility: NotRequired[str]
    pushed_at: Union[datetime, None]
    created_at: Union[datetime, None]
    updated_at: Union[datetime, None]
    allow_rebase_merge: NotRequired[bool]
    temp_clone_token: NotRequired[Union[str, None]]
    allow_squash_merge: NotRequired[bool]
    allow_auto_merge: NotRequired[bool]
    delete_branch_on_merge: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_forking: NotRequired[bool]
    web_commit_signoff_required: NotRequired[bool]
    subscribers_count: NotRequired[int]
    network_count: NotRequired[int]
    open_issues: int
    watchers: int
    master_branch: NotRequired[str]


class TeamRepositoryPropPermissionsType(TypedDict):
    """TeamRepositoryPropPermissions"""

    admin: bool
    pull: bool
    triage: NotRequired[bool]
    push: bool
    maintain: NotRequired[bool]


__all__ = (
    "TeamRepositoryType",
    "TeamRepositoryPropPermissionsType",
)
