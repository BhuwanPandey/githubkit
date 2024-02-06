"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class RepositoryRuleTagNamePatternPropParameters(GitHubModel):
    """RepositoryRuleTagNamePatternPropParameters"""

    name: Missing[str] = Field(
        default=UNSET, description="How this rule will appear to users."
    )
    negate: Missing[bool] = Field(
        default=UNSET, description="If true, the rule will fail if the pattern matches."
    )
    operator: Literal["starts_with", "ends_with", "contains", "regex"] = Field(
        description="The operator to use for matching."
    )
    pattern: str = Field(description="The pattern to match with.")


model_rebuild(RepositoryRuleTagNamePatternPropParameters)

__all__ = ("RepositoryRuleTagNamePatternPropParameters",)
