"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0001 import SimpleUser


class SimpleRepository(GitHubModel):
    """Simple Repository

    A GitHub repository.
    """

    id: int = Field(description="A unique identifier of the repository.")
    node_id: str = Field(description="The GraphQL identifier of the repository.")
    name: str = Field(description="The name of the repository.")
    full_name: str = Field(
        description="The full, globally unique, name of the repository."
    )
    owner: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    private: bool = Field(description="Whether the repository is private.")
    html_url: str = Field(description="The URL to view the repository on GitHub.com.")
    description: Union[str, None] = Field(description="The repository description.")
    fork: bool = Field(description="Whether the repository is a fork.")
    url: str = Field(
        description="The URL to get more information about the repository from the GitHub API."
    )
    archive_url: str = Field(
        description="A template for the API URL to download the repository as an archive."
    )
    assignees_url: str = Field(
        description="A template for the API URL to list the available assignees for issues in the repository."
    )
    blobs_url: str = Field(
        description="A template for the API URL to create or retrieve a raw Git blob in the repository."
    )
    branches_url: str = Field(
        description="A template for the API URL to get information about branches in the repository."
    )
    collaborators_url: str = Field(
        description="A template for the API URL to get information about collaborators of the repository."
    )
    comments_url: str = Field(
        description="A template for the API URL to get information about comments on the repository."
    )
    commits_url: str = Field(
        description="A template for the API URL to get information about commits on the repository."
    )
    compare_url: str = Field(
        description="A template for the API URL to compare two commits or refs."
    )
    contents_url: str = Field(
        description="A template for the API URL to get the contents of the repository."
    )
    contributors_url: str = Field(
        description="A template for the API URL to list the contributors to the repository."
    )
    deployments_url: str = Field(
        description="The API URL to list the deployments of the repository."
    )
    downloads_url: str = Field(
        description="The API URL to list the downloads on the repository."
    )
    events_url: str = Field(
        description="The API URL to list the events of the repository."
    )
    forks_url: str = Field(
        description="The API URL to list the forks of the repository."
    )
    git_commits_url: str = Field(
        description="A template for the API URL to get information about Git commits of the repository."
    )
    git_refs_url: str = Field(
        description="A template for the API URL to get information about Git refs of the repository."
    )
    git_tags_url: str = Field(
        description="A template for the API URL to get information about Git tags of the repository."
    )
    issue_comment_url: str = Field(
        description="A template for the API URL to get information about issue comments on the repository."
    )
    issue_events_url: str = Field(
        description="A template for the API URL to get information about issue events on the repository."
    )
    issues_url: str = Field(
        description="A template for the API URL to get information about issues on the repository."
    )
    keys_url: str = Field(
        description="A template for the API URL to get information about deploy keys on the repository."
    )
    labels_url: str = Field(
        description="A template for the API URL to get information about labels of the repository."
    )
    languages_url: str = Field(
        description="The API URL to get information about the languages of the repository."
    )
    merges_url: str = Field(
        description="The API URL to merge branches in the repository."
    )
    milestones_url: str = Field(
        description="A template for the API URL to get information about milestones of the repository."
    )
    notifications_url: str = Field(
        description="A template for the API URL to get information about notifications on the repository."
    )
    pulls_url: str = Field(
        description="A template for the API URL to get information about pull requests on the repository."
    )
    releases_url: str = Field(
        description="A template for the API URL to get information about releases on the repository."
    )
    stargazers_url: str = Field(
        description="The API URL to list the stargazers on the repository."
    )
    statuses_url: str = Field(
        description="A template for the API URL to get information about statuses of a commit."
    )
    subscribers_url: str = Field(
        description="The API URL to list the subscribers on the repository."
    )
    subscription_url: str = Field(
        description="The API URL to subscribe to notifications for this repository."
    )
    tags_url: str = Field(
        description="The API URL to get information about tags on the repository."
    )
    teams_url: str = Field(
        description="The API URL to list the teams on the repository."
    )
    trees_url: str = Field(
        description="A template for the API URL to create or retrieve a raw Git tree of the repository."
    )
    hooks_url: str = Field(
        description="The API URL to list the hooks on the repository."
    )


model_rebuild(SimpleRepository)

__all__ = ("SimpleRepository",)
