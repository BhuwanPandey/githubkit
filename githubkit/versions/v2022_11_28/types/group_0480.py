"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0479 import (
    WebhookIssueCommentEditedPropIssueAllof0PropPerformedViaGithubAppPropOwnerType,
    WebhookIssueCommentEditedPropIssueAllof0PropPerformedViaGithubAppPropPermissionsType,
)


class WebhookIssueCommentEditedPropIssueAllof0PropPerformedViaGithubAppType(TypedDict):
    """App

    GitHub apps are a new way to extend GitHub. They can be installed directly on
    organizations and user accounts and granted access to specific repositories.
    They come with granular permissions and built-in webhooks. GitHub apps are first
    class actors within GitHub.
    """

    created_at: Union[datetime, None]
    description: Union[str, None]
    events: NotRequired[
        List[
            Literal[
                "branch_protection_rule",
                "check_run",
                "check_suite",
                "code_scanning_alert",
                "commit_comment",
                "content_reference",
                "create",
                "delete",
                "deployment",
                "deployment_review",
                "deployment_status",
                "deploy_key",
                "discussion",
                "discussion_comment",
                "fork",
                "gollum",
                "issues",
                "issue_comment",
                "label",
                "member",
                "membership",
                "milestone",
                "organization",
                "org_block",
                "page_build",
                "project",
                "project_card",
                "project_column",
                "public",
                "pull_request",
                "pull_request_review",
                "pull_request_review_comment",
                "push",
                "registry_package",
                "release",
                "repository",
                "repository_dispatch",
                "secret_scanning_alert",
                "star",
                "status",
                "team",
                "team_add",
                "watch",
                "workflow_dispatch",
                "workflow_run",
                "reminder",
                "pull_request_review_thread",
            ]
        ]
    ]
    external_url: Union[str, None]
    html_url: str
    id: Union[int, None]
    name: str
    node_id: str
    owner: Union[
        WebhookIssueCommentEditedPropIssueAllof0PropPerformedViaGithubAppPropOwnerType,
        None,
    ]
    permissions: NotRequired[
        WebhookIssueCommentEditedPropIssueAllof0PropPerformedViaGithubAppPropPermissionsType
    ]
    slug: NotRequired[str]
    updated_at: Union[datetime, None]


__all__ = ("WebhookIssueCommentEditedPropIssueAllof0PropPerformedViaGithubAppType",)
