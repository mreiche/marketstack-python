import os

from marketstack.api.dividends import dividends
from marketstack.client import Client
from tests.setup import create_client, last_january, last_december

client: Client


def setup_module():
    global client
    client = create_client()


def test_dividends():
    response = dividends.sync(
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbols="AAPL",
        date_from=last_january,
        date_to=last_december,
    )
    assert response.pagination.count > 0
    assert response.data[0].dividend > 0
    assert response.data[0].symbol == "AAPL"
