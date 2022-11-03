import os

from marketstack.api.tickers import (
    ticker_symbol_eod,
    ticker_symbol_intraday,
    ticker_symbol_intraday_latest,
)
from marketstack.client import Client
from marketstack.models import ErrorResponse

from tests.setup import create_client

client: Client


def setup_module():
    global client
    client = create_client()


def test_ticker_symbol_eod():
    response = ticker_symbol_eod.sync(
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbol="AAPL",
    )
    assert isinstance(response, ErrorResponse) is False
    assert response.data.has_eod is True
    assert response.data.eod[0].symbol == "AAPL"


def test_ticker_symbol_intraday():
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
    response = ticker_symbol_intraday_latest.sync(
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbol="AAPL",
    )
    assert response.symbol == "AAPL"
    assert response.open_ > 0
