"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict


class ContentSubmoduleType(TypedDict):
    """Submodule Content

    An object describing a submodule
    """

    type: Literal["submodule"]
    submodule_git_url: str
    size: int
    name: str
    path: str
    sha: str
    url: str
    git_url: Union[str, None]
    html_url: Union[str, None]
    download_url: Union[str, None]
    links: ContentSubmodulePropLinksType


class ContentSubmodulePropLinksType(TypedDict):
    """ContentSubmodulePropLinks"""

    git: Union[str, None]
    html: Union[str, None]
    self_: str


__all__ = (
    "ContentSubmoduleType",
    "ContentSubmodulePropLinksType",
)
