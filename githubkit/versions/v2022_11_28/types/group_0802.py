"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict, NotRequired


class WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropReferencedWorkflowsItemsType(
    TypedDict
):
    """WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropReferencedWorkflowsItems"""

    path: str
    ref: NotRequired[str]
    sha: str


__all__ = (
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropReferencedWorkflowsItemsType",
)
