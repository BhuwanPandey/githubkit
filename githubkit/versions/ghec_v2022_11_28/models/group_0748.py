"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0139 import RepositoryRuleUpdate
from .group_0165 import RepositoryRuleOneof18
from .group_0161 import RepositoryRuleWorkflows
from .group_0142 import RepositoryRuleMergeQueue
from .group_0146 import RepositoryRulePullRequest
from .group_0163 import RepositoryRuleCodeScanning
from .group_0158 import RepositoryRuleTagNamePattern
from .group_0156 import RepositoryRuleBranchNamePattern
from .group_0144 import RepositoryRuleRequiredDeployments
from .group_0148 import RepositoryRuleRequiredStatusChecks
from .group_0150 import RepositoryRuleCommitMessagePattern
from .group_0154 import RepositoryRuleCommitterEmailPattern
from .group_0152 import RepositoryRuleCommitAuthorEmailPattern
from .group_0141 import RepositoryRuleOneof16, RepositoryRuleRequiredLinearHistory
from .group_0138 import (
    RepositoryRuleOneof15,
    RepositoryRuleOneof17,
    RepositoryRuleCreation,
    RepositoryRuleDeletion,
    RepositoryRuleNonFastForward,
    RepositoryRuleRequiredSignatures,
)


class WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItems(GitHubModel):
    """WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItems"""

    rule: Missing[
        Union[
            RepositoryRuleCreation,
            RepositoryRuleUpdate,
            RepositoryRuleDeletion,
            RepositoryRuleRequiredLinearHistory,
            RepositoryRuleMergeQueue,
            RepositoryRuleRequiredDeployments,
            RepositoryRuleRequiredSignatures,
            RepositoryRulePullRequest,
            RepositoryRuleRequiredStatusChecks,
            RepositoryRuleNonFastForward,
            RepositoryRuleCommitMessagePattern,
            RepositoryRuleCommitAuthorEmailPattern,
            RepositoryRuleCommitterEmailPattern,
            RepositoryRuleBranchNamePattern,
            RepositoryRuleTagNamePattern,
            RepositoryRuleOneof15,
            RepositoryRuleOneof16,
            RepositoryRuleOneof17,
            RepositoryRuleOneof18,
            RepositoryRuleWorkflows,
            RepositoryRuleCodeScanning,
        ]
    ] = Field(default=UNSET, title="Repository Rule", description="A repository rule.")
    changes: Missing[
        WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChanges
    ] = Field(default=UNSET)


class WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChanges(
    GitHubModel
):
    """WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChanges"""

    configuration: Missing[
        WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropConfiguration
    ] = Field(default=UNSET)
    rule_type: Missing[
        WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropRuleType
    ] = Field(default=UNSET)
    pattern: Missing[
        WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropPattern
    ] = Field(default=UNSET)


class WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropConfiguration(
    GitHubModel
):
    """WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPro
    pConfiguration
    """

    from_: Missing[str] = Field(default=UNSET, alias="from")


class WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropRuleType(
    GitHubModel
):
    """WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPro
    pRuleType
    """

    from_: Missing[str] = Field(default=UNSET, alias="from")


class WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropPattern(
    GitHubModel
):
    """WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPro
    pPattern
    """

    from_: Missing[str] = Field(default=UNSET, alias="from")


model_rebuild(WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItems)
model_rebuild(
    WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChanges
)
model_rebuild(
    WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropConfiguration
)
model_rebuild(
    WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropRuleType
)
model_rebuild(
    WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropPattern
)

__all__ = (
    "WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItems",
    "WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChanges",
    "WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropConfiguration",
    "WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropRuleType",
    "WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropPattern",
)
