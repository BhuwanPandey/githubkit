"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ReactionRollup(GitHubModel):
    """Reaction Rollup"""

    url: str = Field()
    total_count: int = Field()
    plus_one: int = Field(alias="+1")
    minus_one: int = Field(alias="-1")
    laugh: int = Field()
    confused: int = Field()
    heart: int = Field()
    hooray: int = Field()
    eyes: int = Field()
    rocket: int = Field()


model_rebuild(ReactionRollup)

__all__ = ("ReactionRollup",)
