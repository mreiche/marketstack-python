from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_response_exchange_tickers import PagedResponseExchangeTickers
from ...types import UNSET, Response


def _get_kwargs(
    mic: str,
    *,
    client: Client,
    access_key: str,
) -> Dict[str, Any]:
    url = "{}/exchanges/{mic}/tickers".format(client.base_url, mic=mic)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["access_key"] = access_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[ErrorResponse, HTTPValidationError, PagedResponseExchangeTickers]]:
    if response.status_code == 200:
        response_200 = PagedResponseExchangeTickers.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429
    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[ErrorResponse, HTTPValidationError, PagedResponseExchangeTickers]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    mic: str,
    *,
    client: Client,
    access_key: str,
) -> Response[Union[ErrorResponse, HTTPValidationError, PagedResponseExchangeTickers]]:
    """Tickers

    Args:
        mic (str):
        access_key (str):

    Returns:
        Response[Union[ErrorResponse, HTTPValidationError, PagedResponseExchangeTickers]]
    """

    kwargs = _get_kwargs(
        mic=mic,
        client=client,
        access_key=access_key,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    mic: str,
    *,
    client: Client,
    access_key: str,
) -> Optional[Union[ErrorResponse, HTTPValidationError, PagedResponseExchangeTickers]]:
    """Tickers

    Args:
        mic (str):
        access_key (str):

    Returns:
        Response[Union[ErrorResponse, HTTPValidationError, PagedResponseExchangeTickers]]
    """

    return sync_detailed(
        mic=mic,
        client=client,
        access_key=access_key,
    ).parsed


async def asyncio_detailed(
    mic: str,
    *,
    client: Client,
    access_key: str,
) -> Response[Union[ErrorResponse, HTTPValidationError, PagedResponseExchangeTickers]]:
    """Tickers

    Args:
        mic (str):
        access_key (str):

    Returns:
        Response[Union[ErrorResponse, HTTPValidationError, PagedResponseExchangeTickers]]
    """

    kwargs = _get_kwargs(
        mic=mic,
        client=client,
        access_key=access_key,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    mic: str,
    *,
    client: Client,
    access_key: str,
) -> Optional[Union[ErrorResponse, HTTPValidationError, PagedResponseExchangeTickers]]:
    """Tickers

    Args:
        mic (str):
        access_key (str):

    Returns:
        Response[Union[ErrorResponse, HTTPValidationError, PagedResponseExchangeTickers]]
    """

    return (
        await asyncio_detailed(
            mic=mic,
            client=client,
            access_key=access_key,
        )
    ).parsed
