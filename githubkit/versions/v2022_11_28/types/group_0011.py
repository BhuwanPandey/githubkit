"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import TypedDict, NotRequired


class HookDeliveryType(TypedDict):
    """Webhook delivery

    Delivery made by a webhook.
    """

    id: int
    guid: str
    delivered_at: datetime
    redelivery: bool
    duration: float
    status: str
    status_code: int
    event: str
    action: Union[str, None]
    installation_id: Union[int, None]
    repository_id: Union[int, None]
    url: NotRequired[str]
    request: HookDeliveryPropRequestType
    response: HookDeliveryPropResponseType


class HookDeliveryPropRequestType(TypedDict):
    """HookDeliveryPropRequest"""

    headers: Union[HookDeliveryPropRequestPropHeadersType, None]
    payload: Union[HookDeliveryPropRequestPropPayloadType, None]


class HookDeliveryPropRequestPropHeadersType(TypedDict):
    """HookDeliveryPropRequestPropHeaders

    The request headers sent with the webhook delivery.
    """


class HookDeliveryPropRequestPropPayloadType(TypedDict):
    """HookDeliveryPropRequestPropPayload

    The webhook payload.
    """


class HookDeliveryPropResponseType(TypedDict):
    """HookDeliveryPropResponse"""

    headers: Union[HookDeliveryPropResponsePropHeadersType, None]
    payload: Union[str, None]


class HookDeliveryPropResponsePropHeadersType(TypedDict):
    """HookDeliveryPropResponsePropHeaders

    The response headers received when the delivery was made.
    """


__all__ = (
    "HookDeliveryType",
    "HookDeliveryPropRequestType",
    "HookDeliveryPropRequestPropHeadersType",
    "HookDeliveryPropRequestPropPayloadType",
    "HookDeliveryPropResponseType",
    "HookDeliveryPropResponsePropHeadersType",
)
