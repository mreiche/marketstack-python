import os

from marketstack.api.splits import splits
from marketstack.client import Client
from tests.setup import create_client

client: Client


def setup_module():
    global client
    client = create_client()


def test_splits():
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
