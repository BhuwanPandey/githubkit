"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired


class SelectedActionsType(TypedDict):
    """SelectedActions"""

    github_owned_allowed: NotRequired[bool]
    verified_allowed: NotRequired[bool]
    patterns_allowed: NotRequired[List[str]]


__all__ = ("SelectedActionsType",)
