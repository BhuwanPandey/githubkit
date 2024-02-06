"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0161 import WorkflowRunType


class ReposOwnerRepoActionsWorkflowsWorkflowIdRunsGetResponse200Type(TypedDict):
    """ReposOwnerRepoActionsWorkflowsWorkflowIdRunsGetResponse200"""

    total_count: int
    workflow_runs: List[WorkflowRunType]


__all__ = ("ReposOwnerRepoActionsWorkflowsWorkflowIdRunsGetResponse200Type",)
