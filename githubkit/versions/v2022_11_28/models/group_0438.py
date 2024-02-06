"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0359 import SimpleUserWebhooks


class WebhookGithubAppAuthorizationRevoked(GitHubModel):
    """github_app_authorization revoked event"""

    action: Literal["revoked"] = Field()
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


model_rebuild(WebhookGithubAppAuthorizationRevoked)

__all__ = ("WebhookGithubAppAuthorizationRevoked",)
