from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_response_listmodels_split import PagedResponseListmodelsSplit
from ...models.sort import Sort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    symbol: str,
    *,
    client: Client,
    access_key: str,
    sort: Union[Unset, None, Sort] = UNSET,
    date_from: Union[Unset, None, str] = UNSET,
    date_to: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/tickers/{symbol}/splits".format(client.base_url, symbol=symbol)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["access_key"] = access_key

    json_sort: Union[Unset, None, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value if sort else None

    params["sort"] = json_sort

    params["date_from"] = date_from

    params["date_to"] = date_to

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
) -> Optional[Union[ErrorResponse, HTTPValidationError, PagedResponseListmodelsSplit]]:
    if response.status_code == 200:
        response_200 = PagedResponseListmodelsSplit.from_dict(response.json())

        return response_200
    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[ErrorResponse, HTTPValidationError, PagedResponseListmodelsSplit]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    symbol: str,
    *,
    client: Client,
    access_key: str,
    sort: Union[Unset, None, Sort] = UNSET,
    date_from: Union[Unset, None, str] = UNSET,
    date_to: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorResponse, HTTPValidationError, PagedResponseListmodelsSplit]]:
    """Symbol Splits

    Args:
        symbol (str):
        access_key (str):
        sort (Union[Unset, None, Sort]): An enumeration.
        date_from (Union[Unset, None, str]): Date in the formats %Y-%m-%d, %Y-%m-%d %H:%M:%S or
            ISO-8601 %Y-%m-%dT%H:%M:%S+%Z
        date_to (Union[Unset, None, str]): Date in the formats %Y-%m-%d, %Y-%m-%d %H:%M:%S or
            ISO-8601 %Y-%m-%dT%H:%M:%S+%Z

    Returns:
        Response[Union[ErrorResponse, HTTPValidationError, PagedResponseListmodelsSplit]]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        client=client,
        access_key=access_key,
        sort=sort,
        date_from=date_from,
        date_to=date_to,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    symbol: str,
    *,
    client: Client,
    access_key: str,
    sort: Union[Unset, None, Sort] = UNSET,
    date_from: Union[Unset, None, str] = UNSET,
    date_to: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorResponse, HTTPValidationError, PagedResponseListmodelsSplit]]:
    """Symbol Splits

    Args:
        symbol (str):
        access_key (str):
        sort (Union[Unset, None, Sort]): An enumeration.
        date_from (Union[Unset, None, str]): Date in the formats %Y-%m-%d, %Y-%m-%d %H:%M:%S or
            ISO-8601 %Y-%m-%dT%H:%M:%S+%Z
        date_to (Union[Unset, None, str]): Date in the formats %Y-%m-%d, %Y-%m-%d %H:%M:%S or
            ISO-8601 %Y-%m-%dT%H:%M:%S+%Z

    Returns:
        Response[Union[ErrorResponse, HTTPValidationError, PagedResponseListmodelsSplit]]
    """

    return sync_detailed(
        symbol=symbol,
        client=client,
        access_key=access_key,
        sort=sort,
        date_from=date_from,
        date_to=date_to,
    ).parsed


async def asyncio_detailed(
    symbol: str,
    *,
    client: Client,
    access_key: str,
    sort: Union[Unset, None, Sort] = UNSET,
    date_from: Union[Unset, None, str] = UNSET,
    date_to: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorResponse, HTTPValidationError, PagedResponseListmodelsSplit]]:
    """Symbol Splits

    Args:
        symbol (str):
        access_key (str):
        sort (Union[Unset, None, Sort]): An enumeration.
        date_from (Union[Unset, None, str]): Date in the formats %Y-%m-%d, %Y-%m-%d %H:%M:%S or
            ISO-8601 %Y-%m-%dT%H:%M:%S+%Z
        date_to (Union[Unset, None, str]): Date in the formats %Y-%m-%d, %Y-%m-%d %H:%M:%S or
            ISO-8601 %Y-%m-%dT%H:%M:%S+%Z

    Returns:
        Response[Union[ErrorResponse, HTTPValidationError, PagedResponseListmodelsSplit]]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        client=client,
        access_key=access_key,
        sort=sort,
        date_from=date_from,
        date_to=date_to,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    symbol: str,
    *,
    client: Client,
    access_key: str,
    sort: Union[Unset, None, Sort] = UNSET,
    date_from: Union[Unset, None, str] = UNSET,
    date_to: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorResponse, HTTPValidationError, PagedResponseListmodelsSplit]]:
    """Symbol Splits

    Args:
        symbol (str):
        access_key (str):
        sort (Union[Unset, None, Sort]): An enumeration.
        date_from (Union[Unset, None, str]): Date in the formats %Y-%m-%d, %Y-%m-%d %H:%M:%S or
            ISO-8601 %Y-%m-%dT%H:%M:%S+%Z
        date_to (Union[Unset, None, str]): Date in the formats %Y-%m-%d, %Y-%m-%d %H:%M:%S or
            ISO-8601 %Y-%m-%dT%H:%M:%S+%Z

    Returns:
        Response[Union[ErrorResponse, HTTPValidationError, PagedResponseListmodelsSplit]]
    """

    return (
        await asyncio_detailed(
            symbol=symbol,
            client=client,
            access_key=access_key,
            sort=sort,
            date_from=date_from,
            date_to=date_to,
        )
    ).parsed
