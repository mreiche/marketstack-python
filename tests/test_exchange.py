import os

from marketstack.api.exchanges import (
    exchange_mic,
    exchange_mic_eod,
    exchange_mic_eod_date,
    exchange_mic_eod_latest,
    exchange_mic_intraday,
    exchange_mic_intraday_date,
    exchange_mic_intraday_latest,
    exchange_mic_tickers,
    exchanges,
)
from marketstack.client import Client
from marketstack.models import ErrorResponse
from tests.setup import create_client, day_format, this_january

client: Client


def setup_module():
    global client
    client = create_client()


def test_exchanges():
    response = exchanges.sync(
        client=client,
        search="Xetra",
        access_key=os.getenv("MARKETSTACK_API_KEY"),
    )
    assert isinstance(response, ErrorResponse) is False
    assert response.pagination.count == 1
    assert response.data[0].mic == "XETRA"


def test_exchange_mic():
    response = exchange_mic.sync(
        client=client,
        mic="XETRA",
        access_key=os.getenv("MARKETSTACK_API_KEY"),
    )
    assert isinstance(response, ErrorResponse) is False
    assert response.mic == "XETRA"


def test_exchange_mic_tickers():
    response = exchange_mic_tickers.sync(
        client=client,
        mic="XETRA",
        access_key=os.getenv("MARKETSTACK_API_KEY"),
    )
    assert isinstance(response, ErrorResponse) is False
    assert response.data.mic == "XETRA"
    assert len(response.data.tickers) > 0


def test_exchanges_mic_eod():
    response = exchange_mic_eod.sync(
        mic="XNAS",
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbols="AAPL",
        limit=1,
    )
    assert isinstance(response, ErrorResponse) is False
    assert response.pagination.count == 1
    assert response.data.mic == "XNAS"
    assert response.data.eod[0].exchange == "XNAS"
    assert response.data.eod[0].symbol == "AAPL"


def test_exchanges_mic_eod_date():
    response = exchange_mic_eod_date.sync(
        mic="XNAS",
        date=this_january,
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbols="AAPL",
    )
    assert isinstance(response, ErrorResponse) is False
    assert response.data.mic == "XNAS"
    assert response.data.eod[0].symbol == "AAPL"
    assert response.data.eod[0].exchange == "XNAS"
    assert response.data.eod[0].date.strftime(day_format) == this_january


def test_exchanges_mic_eod_latest():
    response = exchange_mic_eod_latest.sync(
        mic="XNAS",
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbols="AAPL",
    )
    assert isinstance(response, ErrorResponse) is False
    assert response.data.mic == "XNAS"
    assert response.data.eod[0].symbol == "AAPL"
    assert response.data.eod[0].exchange == "XNAS"


def test_exchanges_mic_intraday():
    response = exchange_mic_intraday.sync(
        mic="XNAS",
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbols="AAPL",
        limit=1,
    )
    assert response.pagination.count == 1
    assert response.data.intraday[0].symbol == "AAPL"


def test_exchanges_mic_intraday_date():
    response = exchange_mic_intraday_date.sync(
        mic="XNAS",
        date=this_january,
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbols="AAPL"
    )
    assert response.pagination.count > 0
    assert response.data.intraday[0].symbol == "AAPL"
    assert response.data.intraday[0].date.strftime(day_format) == this_january


def test_exchanges_mic_intraday_latest():
    response = exchange_mic_intraday_latest.sync(
        mic="XNAS",
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbols="AAPL"
    )
    assert response.pagination.count > 0
    assert response.data.intraday[0].symbol == "AAPL"
