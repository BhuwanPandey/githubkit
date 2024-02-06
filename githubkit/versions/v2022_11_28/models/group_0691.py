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
from githubkit.compat import GitHubModel, model_rebuild

from .group_0694 import WebhookReleasePrereleasedPropReleaseAllof0PropReactions
from .group_0692 import WebhookReleasePrereleasedPropReleaseAllof0PropAssetsItems


class WebhookReleasePrereleasedPropReleaseAllof0(GitHubModel):
    """Release

    The [release](https://docs.github.com/rest/releases/releases/#get-a-release)
    object.
    """

    assets: List[WebhookReleasePrereleasedPropReleaseAllof0PropAssetsItems] = Field()
    assets_url: str = Field()
    author: Union[WebhookReleasePrereleasedPropReleaseAllof0PropAuthor, None] = Field(
        title="User"
    )
    body: Union[str, None] = Field()
    created_at: Union[datetime, None] = Field()
    discussion_url: Missing[str] = Field(default=UNSET)
    draft: bool = Field(description="Whether the release is a draft or published")
    html_url: str = Field()
    id: int = Field()
    name: Union[str, None] = Field()
    node_id: str = Field()
    prerelease: bool = Field(
        description="Whether the release is identified as a prerelease or a full release."
    )
    published_at: Union[datetime, None] = Field()
    reactions: Missing[WebhookReleasePrereleasedPropReleaseAllof0PropReactions] = Field(
        default=UNSET, title="Reactions"
    )
    tag_name: str = Field(description="The name of the tag.")
    tarball_url: Union[str, None] = Field()
    target_commitish: str = Field(
        description="Specifies the commitish value that determines where the Git tag is created from."
    )
    upload_url: str = Field()
    url: str = Field()
    zipball_url: Union[str, None] = Field()


class WebhookReleasePrereleasedPropReleaseAllof0PropAuthor(GitHubModel):
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


model_rebuild(WebhookReleasePrereleasedPropReleaseAllof0)
model_rebuild(WebhookReleasePrereleasedPropReleaseAllof0PropAuthor)

__all__ = (
    "WebhookReleasePrereleasedPropReleaseAllof0",
    "WebhookReleasePrereleasedPropReleaseAllof0PropAuthor",
)
