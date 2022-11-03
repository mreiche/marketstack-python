import os
from pathlib import Path

from dotenv import load_dotenv
from marketstack.api.currencies import currencies
from marketstack.api.dividends import dividends
from marketstack.api.eod import eod, eod_latest
from marketstack.api.exchanges import exchange_mic_eod_date, exchange_mic_intraday_date
from marketstack.api.splits import splits
from marketstack.api.tickers import (
    ticker_symbol_eod,
    ticker_symbol_intraday,
    ticker_symbol_intraday_latest,
)
from marketstack.api.timezones import timezones
from marketstack.client import Client
from marketstack.models import ErrorCode, ErrorResponse


def setup_module():
    assert load_dotenv(Path(__file__).parent / "test.env") is True


def create_client():
    tls_support = os.getenv("MARKETSTACK_TLS_SUPPORT")
    access_key = os.getenv("MARKETSTACK_API_KEY")
    assert (
        access_key is not None and len(access_key) > 0
    ), "Environment variable MARKETSTACK_API_KEY is not defined"
    protocol = "https" if tls_support == "1" else "http"
    return Client(base_url=f"{protocol}://api.marketstack.com/v1")


def test_eod():
    client = create_client()
    response = eod.sync(
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbols="AAPL,AMZN",
        limit=10,
    )
    aapl = None
    amzn = None
    for price in response.data:
        if price.symbol == "AAPL":
            aapl = price
        elif price.symbol == "AMZN":
            amzn = price

    assert response.pagination.limit == 10
    assert response.pagination.count == 10
    assert aapl.open_ > 0
    assert aapl.exchange == "XNAS"
    assert amzn.open_ > 0
    assert amzn.exchange == "XNAS"
    # assert aapl.date.isoformat() == "2022-01-01T00:00:00+00:00"


def test_eod_latest():
    client = create_client()
    response = eod_latest.sync(
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbols="AAPL",
    )
    assert response.pagination.count == 1
    assert response.data[0].symbol == "AAPL"


def test_ticker_symbol_eod():
    client = create_client()
    response = ticker_symbol_eod.sync(
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbol="AAPL",
    )
    assert response.data.has_eod is True
    assert response.data.eod[0].symbol == "AAPL"


def test_ticker_symbol_intraday():
    client = create_client()
    response = ticker_symbol_intraday.sync(
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbol="AAPL",
        limit=1,
    )
    assert response.pagination.count == 1
    assert response.data.has_intraday is True
    assert response.data.intraday[0].symbol == "AAPL"


def test_ticker_symbol_intraday_latest():
    client = create_client()
    response = ticker_symbol_intraday_latest.sync(
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbol="AAPL",
    )
    assert response.symbol == "AAPL"
    assert response.open_ > 0


def test_splits():
    client = create_client()
    response = splits.sync(
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbols="AAPL",
        date_to="2022-01-01",
    )
    assert response.pagination.count == 5
    assert response.data[0].date == "2020-08-31"
    assert response.data[0].split_factor > 0
    assert response.data[0].symbol == "AAPL"


def test_dividends():
    client = create_client()
    response = dividends.sync(
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbols="AAPL",
        date_from="2020-01-01 00:00:00",
        date_to="2020-12-31 00:00:00",
    )
    assert response.pagination.count == 4
    assert response.data[0].date == "2020-11-06"
    assert response.data[0].dividend > 0
    assert response.data[0].symbol == "AAPL"


def test_currencies():
    client = create_client()
    response = currencies.sync(
        client=client, access_key=os.getenv("MARKETSTACK_API_KEY"), limit=1
    )
    assert response.pagination.count == 1
    assert response.data[0].symbol == "$"
    assert response.data[0].code == "USD"


def test_timezones():
    client = create_client()
    response = timezones.sync(
        client=client, access_key=os.getenv("MARKETSTACK_API_KEY"), limit=1
    )
    assert response.pagination.count == 1
    assert response.data[0].timezone == "America/New_York"


def test_exchanges_mic_eod_date():
    client = create_client()
    response = exchange_mic_eod_date.sync(
        mic="XNAS",
        date="2020-12-31",
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
    )
    assert isinstance(response, ErrorResponse)
    assert response.error.code == ErrorCode.FUNCTION_ACCESS_RESTRICTED


def test_exchanges_mic_intraday_date():
    client = create_client()
    response = exchange_mic_intraday_date.sync(
        mic="XNAS",
        date="2020-12-31",
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbols="AAPL",
        limit=1,
    )
    assert response.pagination.count == 1
    assert response.data.intraday[0].symbol == "AAPL"
