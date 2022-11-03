import os

from marketstack.api.dividends import dividends
from marketstack.client import Client
from tests.setup import create_client

client: Client


def setup_module():
    global client
    client = create_client()


def test_dividends():
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
