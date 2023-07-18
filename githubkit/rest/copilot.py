"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

    python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from typing import TYPE_CHECKING, Dict, List, Literal, Optional, overload

from pydantic import BaseModel, parse_obj_as

from githubkit.utils import UNSET, Missing, exclude_unset

from .types import (
    OrgsOrgCopilotBillingSelectedTeamsPostBodyType,
    OrgsOrgCopilotBillingSelectedUsersPostBodyType,
    OrgsOrgCopilotBillingSelectedTeamsDeleteBodyType,
    OrgsOrgCopilotBillingSelectedUsersDeleteBodyType,
)
from .models import (
    BasicError,
    CopilotSeatDetails,
    CopilotOrganizationDetails,
    OrgsOrgCopilotBillingSelectedTeamsPostBody,
    OrgsOrgCopilotBillingSelectedUsersPostBody,
    OrgsOrgCopilotBillingSelectedTeamsDeleteBody,
    OrgsOrgCopilotBillingSelectedUsersDeleteBody,
    OrganizationsOrgCopilotBillingSeatsGetResponse200,
    OrgsOrgCopilotBillingSelectedTeamsPostResponse201,
    OrgsOrgCopilotBillingSelectedUsersPostResponse201,
    OrgsOrgCopilotBillingSelectedTeamsDeleteResponse200,
    OrgsOrgCopilotBillingSelectedUsersDeleteResponse200,
)

if TYPE_CHECKING:
    from githubkit import GitHubCore
    from githubkit.response import Response


class CopilotClient:
    _REST_API_VERSION = "2022-11-28"

    def __init__(self, github: "GitHubCore"):
        self._github = github

    def get_copilot_organization_details(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[CopilotOrganizationDetails]":
        url = f"/organizations/{org}/copilot/billing"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CopilotOrganizationDetails,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    async def async_get_copilot_organization_details(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[CopilotOrganizationDetails]":
        url = f"/organizations/{org}/copilot/billing"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CopilotOrganizationDetails,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    def list_copilot_seats(
        self,
        org: str,
        page: Missing[int] = 1,
        per_page: Missing[int] = 50,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[OrganizationsOrgCopilotBillingSeatsGetResponse200]":
        url = f"/organizations/{org}/copilot/billing/seats"

        params = {
            "page": page,
            "per_page": per_page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=OrganizationsOrgCopilotBillingSeatsGetResponse200,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    async def async_list_copilot_seats(
        self,
        org: str,
        page: Missing[int] = 1,
        per_page: Missing[int] = 50,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[OrganizationsOrgCopilotBillingSeatsGetResponse200]":
        url = f"/organizations/{org}/copilot/billing/seats"

        params = {
            "page": page,
            "per_page": per_page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=OrganizationsOrgCopilotBillingSeatsGetResponse200,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    @overload
    def add_copilot_for_business_seats_for_teams(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCopilotBillingSelectedTeamsPostBodyType,
    ) -> "Response[OrgsOrgCopilotBillingSelectedTeamsPostResponse201]":
        ...

    @overload
    def add_copilot_for_business_seats_for_teams(
        self,
        org: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        selected_teams: List[str],
    ) -> "Response[OrgsOrgCopilotBillingSelectedTeamsPostResponse201]":
        ...

    def add_copilot_for_business_seats_for_teams(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[OrgsOrgCopilotBillingSelectedTeamsPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[OrgsOrgCopilotBillingSelectedTeamsPostResponse201]":
        url = f"/orgs/{org}/copilot/billing/selected_teams"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(OrgsOrgCopilotBillingSelectedTeamsPostBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=OrgsOrgCopilotBillingSelectedTeamsPostResponse201,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    @overload
    async def async_add_copilot_for_business_seats_for_teams(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCopilotBillingSelectedTeamsPostBodyType,
    ) -> "Response[OrgsOrgCopilotBillingSelectedTeamsPostResponse201]":
        ...

    @overload
    async def async_add_copilot_for_business_seats_for_teams(
        self,
        org: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        selected_teams: List[str],
    ) -> "Response[OrgsOrgCopilotBillingSelectedTeamsPostResponse201]":
        ...

    async def async_add_copilot_for_business_seats_for_teams(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[OrgsOrgCopilotBillingSelectedTeamsPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[OrgsOrgCopilotBillingSelectedTeamsPostResponse201]":
        url = f"/orgs/{org}/copilot/billing/selected_teams"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(OrgsOrgCopilotBillingSelectedTeamsPostBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=OrgsOrgCopilotBillingSelectedTeamsPostResponse201,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    @overload
    def cancel_copilot_seat_assignment_for_teams(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCopilotBillingSelectedTeamsDeleteBodyType,
    ) -> "Response[OrgsOrgCopilotBillingSelectedTeamsDeleteResponse200]":
        ...

    @overload
    def cancel_copilot_seat_assignment_for_teams(
        self,
        org: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        selected_teams: List[str],
    ) -> "Response[OrgsOrgCopilotBillingSelectedTeamsDeleteResponse200]":
        ...

    def cancel_copilot_seat_assignment_for_teams(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[OrgsOrgCopilotBillingSelectedTeamsDeleteBodyType] = UNSET,
        **kwargs,
    ) -> "Response[OrgsOrgCopilotBillingSelectedTeamsDeleteResponse200]":
        url = f"/orgs/{org}/copilot/billing/selected_teams"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(OrgsOrgCopilotBillingSelectedTeamsDeleteBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "DELETE",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=OrgsOrgCopilotBillingSelectedTeamsDeleteResponse200,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    @overload
    async def async_cancel_copilot_seat_assignment_for_teams(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCopilotBillingSelectedTeamsDeleteBodyType,
    ) -> "Response[OrgsOrgCopilotBillingSelectedTeamsDeleteResponse200]":
        ...

    @overload
    async def async_cancel_copilot_seat_assignment_for_teams(
        self,
        org: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        selected_teams: List[str],
    ) -> "Response[OrgsOrgCopilotBillingSelectedTeamsDeleteResponse200]":
        ...

    async def async_cancel_copilot_seat_assignment_for_teams(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[OrgsOrgCopilotBillingSelectedTeamsDeleteBodyType] = UNSET,
        **kwargs,
    ) -> "Response[OrgsOrgCopilotBillingSelectedTeamsDeleteResponse200]":
        url = f"/orgs/{org}/copilot/billing/selected_teams"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(OrgsOrgCopilotBillingSelectedTeamsDeleteBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "DELETE",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=OrgsOrgCopilotBillingSelectedTeamsDeleteResponse200,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    @overload
    def add_copilot_for_business_seats_for_users(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCopilotBillingSelectedUsersPostBodyType,
    ) -> "Response[OrgsOrgCopilotBillingSelectedUsersPostResponse201]":
        ...

    @overload
    def add_copilot_for_business_seats_for_users(
        self,
        org: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        selected_usernames: List[str],
    ) -> "Response[OrgsOrgCopilotBillingSelectedUsersPostResponse201]":
        ...

    def add_copilot_for_business_seats_for_users(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[OrgsOrgCopilotBillingSelectedUsersPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[OrgsOrgCopilotBillingSelectedUsersPostResponse201]":
        url = f"/orgs/{org}/copilot/billing/selected_users"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(OrgsOrgCopilotBillingSelectedUsersPostBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=OrgsOrgCopilotBillingSelectedUsersPostResponse201,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    @overload
    async def async_add_copilot_for_business_seats_for_users(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCopilotBillingSelectedUsersPostBodyType,
    ) -> "Response[OrgsOrgCopilotBillingSelectedUsersPostResponse201]":
        ...

    @overload
    async def async_add_copilot_for_business_seats_for_users(
        self,
        org: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        selected_usernames: List[str],
    ) -> "Response[OrgsOrgCopilotBillingSelectedUsersPostResponse201]":
        ...

    async def async_add_copilot_for_business_seats_for_users(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[OrgsOrgCopilotBillingSelectedUsersPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[OrgsOrgCopilotBillingSelectedUsersPostResponse201]":
        url = f"/orgs/{org}/copilot/billing/selected_users"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(OrgsOrgCopilotBillingSelectedUsersPostBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=OrgsOrgCopilotBillingSelectedUsersPostResponse201,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    @overload
    def cancel_copilot_seat_assignment_for_users(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCopilotBillingSelectedUsersDeleteBodyType,
    ) -> "Response[OrgsOrgCopilotBillingSelectedUsersDeleteResponse200]":
        ...

    @overload
    def cancel_copilot_seat_assignment_for_users(
        self,
        org: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        selected_usernames: List[str],
    ) -> "Response[OrgsOrgCopilotBillingSelectedUsersDeleteResponse200]":
        ...

    def cancel_copilot_seat_assignment_for_users(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[OrgsOrgCopilotBillingSelectedUsersDeleteBodyType] = UNSET,
        **kwargs,
    ) -> "Response[OrgsOrgCopilotBillingSelectedUsersDeleteResponse200]":
        url = f"/orgs/{org}/copilot/billing/selected_users"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(OrgsOrgCopilotBillingSelectedUsersDeleteBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "DELETE",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=OrgsOrgCopilotBillingSelectedUsersDeleteResponse200,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    @overload
    async def async_cancel_copilot_seat_assignment_for_users(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: OrgsOrgCopilotBillingSelectedUsersDeleteBodyType,
    ) -> "Response[OrgsOrgCopilotBillingSelectedUsersDeleteResponse200]":
        ...

    @overload
    async def async_cancel_copilot_seat_assignment_for_users(
        self,
        org: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        selected_usernames: List[str],
    ) -> "Response[OrgsOrgCopilotBillingSelectedUsersDeleteResponse200]":
        ...

    async def async_cancel_copilot_seat_assignment_for_users(
        self,
        org: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[OrgsOrgCopilotBillingSelectedUsersDeleteBodyType] = UNSET,
        **kwargs,
    ) -> "Response[OrgsOrgCopilotBillingSelectedUsersDeleteResponse200]":
        url = f"/orgs/{org}/copilot/billing/selected_users"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(OrgsOrgCopilotBillingSelectedUsersDeleteBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "DELETE",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=OrgsOrgCopilotBillingSelectedUsersDeleteResponse200,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    def get_copilot_seat_assignment_details_for_user(
        self,
        org: str,
        username: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[CopilotSeatDetails]":
        url = f"/orgs/{org}/members/{username}/copilot"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CopilotSeatDetails,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )

    async def async_get_copilot_seat_assignment_details_for_user(
        self,
        org: str,
        username: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[CopilotSeatDetails]":
        url = f"/orgs/{org}/members/{username}/copilot"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CopilotSeatDetails,
            error_models={
                "500": BasicError,
                "401": BasicError,
                "403": BasicError,
                "404": BasicError,
            },
        )
