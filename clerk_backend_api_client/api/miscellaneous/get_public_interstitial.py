from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    frontend_api: Union[Unset, str] = UNSET,
    publishable_key: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["frontendApi"] = frontend_api

    params["publishable_key"] = publishable_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/public/interstitial",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    frontend_api: Union[Unset, str] = UNSET,
    publishable_key: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Returns the markup for the interstitial page

     The Clerk interstitial endpoint serves an html page that loads clerk.js in order to check the user's
    authentication state.
    It is used by Clerk SDKs when the user's authentication state cannot be immediately determined.

    Args:
        frontend_api (Union[Unset, str]):
        publishable_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        frontend_api=frontend_api,
        publishable_key=publishable_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    frontend_api: Union[Unset, str] = UNSET,
    publishable_key: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Returns the markup for the interstitial page

     The Clerk interstitial endpoint serves an html page that loads clerk.js in order to check the user's
    authentication state.
    It is used by Clerk SDKs when the user's authentication state cannot be immediately determined.

    Args:
        frontend_api (Union[Unset, str]):
        publishable_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        frontend_api=frontend_api,
        publishable_key=publishable_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
