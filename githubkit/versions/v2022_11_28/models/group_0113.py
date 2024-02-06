"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class RepositoryRuleRequiredDeploymentsPropParameters(GitHubModel):
    """RepositoryRuleRequiredDeploymentsPropParameters"""

    required_deployment_environments: List[str] = Field(
        description="The environments that must be successfully deployed to before branches can be merged."
    )


model_rebuild(RepositoryRuleRequiredDeploymentsPropParameters)

__all__ = ("RepositoryRuleRequiredDeploymentsPropParameters",)
