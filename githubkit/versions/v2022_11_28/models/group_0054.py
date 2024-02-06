"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ActionsCacheUsageOrgEnterprise(GitHubModel):
    """ActionsCacheUsageOrgEnterprise"""

    total_active_caches_count: int = Field(
        description="The count of active caches across all repositories of an enterprise or an organization."
    )
    total_active_caches_size_in_bytes: int = Field(
        description="The total size in bytes of all active cache items across all repositories of an enterprise or an organization."
    )


model_rebuild(ActionsCacheUsageOrgEnterprise)

__all__ = ("ActionsCacheUsageOrgEnterprise",)
