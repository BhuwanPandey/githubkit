"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0366 import ProjectsV2ItemType
from .group_0356 import SimpleInstallationType
from .group_0359 import SimpleUserWebhooksType
from .group_0357 import OrganizationSimpleWebhooksType


class WebhookProjectsV2ItemRestoredType(TypedDict):
    """Projects v2 Item Restored Event"""

    action: Literal["restored"]
    changes: WebhookProjectsV2ItemRestoredPropChangesType
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    projects_v2_item: ProjectsV2ItemType
    sender: SimpleUserWebhooksType


class WebhookProjectsV2ItemRestoredPropChangesType(TypedDict):
    """WebhookProjectsV2ItemRestoredPropChanges"""

    archived_at: NotRequired[WebhookProjectsV2ItemRestoredPropChangesPropArchivedAtType]


class WebhookProjectsV2ItemRestoredPropChangesPropArchivedAtType(TypedDict):
    """WebhookProjectsV2ItemRestoredPropChangesPropArchivedAt"""

    from_: NotRequired[Union[datetime, None]]
    to: NotRequired[Union[datetime, None]]


__all__ = (
    "WebhookProjectsV2ItemRestoredType",
    "WebhookProjectsV2ItemRestoredPropChangesType",
    "WebhookProjectsV2ItemRestoredPropChangesPropArchivedAtType",
)
