import os

from marketstack.api.tickers import (
    ticker_symbol,
    ticker_symbol_dividends,
    ticker_symbol_eod,
    ticker_symbol_eod_date,
    ticker_symbol_eod_latest,
    ticker_symbol_intraday,
    ticker_symbol_intraday_date,
    ticker_symbol_intraday_latest,
    ticker_symbol_splits,
    tickers,
)
from marketstack.client import Client
from marketstack.models import ErrorResponse, ErrorCode
from tests.setup import create_client, this_january, day_format

client: Client


def setup_module():
    global client
    client = create_client()


def test_tickers():
    response = tickers.sync(
        search="Apple",
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        limit=1,
    )
    assert isinstance(response, ErrorResponse) is False
    assert response.pagination.count == 1
    assert response.data[0].symbol == "AAPL"
    assert len(response.data[0].stock_exchange.mic) > 0


def test_ticker_symbol():
    response = ticker_symbol.sync(
        symbol="AAPL",
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
    )
    assert isinstance(response, ErrorResponse) is False
    assert response.symbol == "AAPL"


def test_ticker_symbol_not_found():
    response = ticker_symbol.sync(
        symbol="AYBABTO",
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
    )
    assert isinstance(response, ErrorResponse) is True
    assert response.error.code == ErrorCode.NOT_FOUND_ERROR


def test_ticker_symbol_dividends():
    response = ticker_symbol_dividends.sync(
        symbol="AAPL",
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
    )
    assert isinstance(response, ErrorResponse) is False
    assert response.data[0].symbol == "AAPL"
    assert response.data[0].dividend > 0


def test_ticker_symbol_splits():
    response = ticker_symbol_splits.sync(
        symbol="AAPL",
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
    )
    assert isinstance(response, ErrorResponse) is False
    assert response.data[0].symbol == "AAPL"
    assert response.data[0].split_factor > 0


def test_ticker_symbol_eod():
    response = ticker_symbol_eod.sync(
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbol="AAPL",
    )
    assert isinstance(response, ErrorResponse) is False
    assert response.data.has_eod is True
    assert response.data.eod[0].symbol == "AAPL"


def test_ticker_symbol_eod_date():
    response = ticker_symbol_eod_date.sync(
        symbol="AAPL",
        client=client,
        date=this_january,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
    )
    assert isinstance(response, ErrorResponse) is False
    assert response.symbol == "AAPL"
    assert response.date.strftime(day_format) == this_january


def test_ticker_symbol_eod_latest():
    response = ticker_symbol_eod_latest.sync(
        symbol="AAPL",
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
    )
    assert isinstance(response, ErrorResponse) is False
    assert response.symbol == "AAPL"


def test_ticker_symbol_intraday():
    response = ticker_symbol_intraday.sync(
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbol="AAPL",
        limit=1,
    )
    assert isinstance(response, ErrorResponse) is False
    assert response.pagination.count == 1
    assert response.data.has_intraday is True
    assert response.data.intraday[0].symbol == "AAPL"


def test_ticker_symbol_intraday_date():
    response = ticker_symbol_intraday_date.sync(
        client=client,
        date=this_january,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbol="AAPL",
    )
    assert isinstance(response, ErrorResponse) is False
    assert response.data[0].symbol == "AAPL"
    assert response.data[0].date.strftime(day_format) == this_january


def test_ticker_symbol_intraday_latest():
    response = ticker_symbol_intraday_latest.sync(
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbol="AAPL",
    )
    assert isinstance(response, ErrorResponse) is False
    assert response.symbol == "AAPL"
    assert response.open_ > 0
