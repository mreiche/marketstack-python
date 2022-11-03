import os

from marketstack.api.exchanges import exchange_mic_eod_date, exchange_mic_intraday_date
from marketstack.client import Client
from marketstack.models import ErrorCode, ErrorResponse
from tests.setup import create_client

client: Client


def setup_module():
    global client
    client = create_client()


def test_exchanges_mic_eod_date():
    response = exchange_mic_eod_date.sync(
        mic="XNAS",
        date="2020-12-31",
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
    )
    assert isinstance(response, ErrorResponse)
    assert response.error.code == ErrorCode.FUNCTION_ACCESS_RESTRICTED


def test_exchanges_mic_intraday_date():
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
