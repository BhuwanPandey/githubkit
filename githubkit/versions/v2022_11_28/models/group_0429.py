"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild

from .group_0362 import Discussion
from .group_0358 import RepositoryWebhooks
from .group_0359 import SimpleUserWebhooks
from .group_0357 import OrganizationSimpleWebhooks


class WebhookDiscussionUnanswered(GitHubModel):
    """discussion unanswered event"""

    action: Literal["unanswered"] = Field()
    discussion: Discussion = Field(
        title="Discussion", description="A Discussion in a repository."
    )
    old_answer: WebhookDiscussionUnansweredPropOldAnswer = Field()
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: Missing[SimpleUserWebhooks] = Field(
        default=UNSET,
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookDiscussionUnansweredPropOldAnswer(GitHubModel):
    """WebhookDiscussionUnansweredPropOldAnswer"""

    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ] = Field(
        title="AuthorAssociation",
        description="How the author is associated with the repository.",
    )
    body: str = Field()
    child_comment_count: int = Field()
    created_at: datetime = Field()
    discussion_id: int = Field()
    html_url: str = Field()
    id: int = Field()
    node_id: str = Field()
    parent_id: None = Field()
    reactions: Missing[WebhookDiscussionUnansweredPropOldAnswerPropReactions] = Field(
        default=UNSET, title="Reactions"
    )
    repository_url: str = Field()
    updated_at: datetime = Field()
    user: Union[WebhookDiscussionUnansweredPropOldAnswerPropUser, None] = Field(
        title="User"
    )


class WebhookDiscussionUnansweredPropOldAnswerPropReactions(GitHubModel):
    """Reactions"""

    plus_one: int = Field(alias="+1")
    minus_one: int = Field(alias="-1")
    confused: int = Field()
    eyes: int = Field()
    heart: int = Field()
    hooray: int = Field()
    laugh: int = Field()
    rocket: int = Field()
    total_count: int = Field()
    url: str = Field()


class WebhookDiscussionUnansweredPropOldAnswerPropUser(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookDiscussionUnanswered)
model_rebuild(WebhookDiscussionUnansweredPropOldAnswer)
model_rebuild(WebhookDiscussionUnansweredPropOldAnswerPropReactions)
model_rebuild(WebhookDiscussionUnansweredPropOldAnswerPropUser)

__all__ = (
    "WebhookDiscussionUnanswered",
    "WebhookDiscussionUnansweredPropOldAnswer",
    "WebhookDiscussionUnansweredPropOldAnswerPropReactions",
    "WebhookDiscussionUnansweredPropOldAnswerPropUser",
)
