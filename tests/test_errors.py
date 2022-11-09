import os
from unittest import mock

from marketstack.api.intraday import intraday
from marketstack.api.tickers import ticker_symbol
from marketstack.api.timezones import timezones
from marketstack.models import ErrorResponse, ErrorCode, Interval
from tests.setup import create_client


@mock.patch.dict(os.environ, {
    "MARKETSTACK_TLS_SUPPORT": "1",
})
def test_tls_not_supported():
    client = create_client()

    response = timezones.sync(
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        limit=1
    )

    assert isinstance(response, ErrorResponse)
    assert response.error.code == ErrorCode.HTTPS_ACCESS_RESTRICTED


@mock.patch.dict(os.environ, {
    "MARKETSTACK_API_KEY": "AYBABTU",
})
def test_invalid_access_key():
    client = create_client()

    response = timezones.sync(
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        limit=1
    )

    assert isinstance(response, ErrorResponse)
    assert response.error.code == ErrorCode.INVALID_ACCESS_KEY


def test_not_found():
    client = create_client()

    response = ticker_symbol.sync(
        symbol="AYBABTU",
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
    )
    assert isinstance(response, ErrorResponse) is True
    assert response.error.code == ErrorCode.NOT_FOUND_ERROR


def test_feature_not_allowed():
    client = create_client()

    response = intraday.sync(
        symbols="AAPL",
        client=client,
        interval=Interval.MIN1,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
    )
    assert isinstance(response, ErrorResponse) is True
    assert response.error.code == ErrorCode.FUNCTION_ACCESS_RESTRICTED
