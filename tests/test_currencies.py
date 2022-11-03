import os

from marketstack.api.currencies import currencies
from marketstack.client import Client

from tests.setup import create_client

client: Client


def setup_module():
    global client
    client = create_client()


def test_currencies():
    response = currencies.sync(
        client=client, access_key=os.getenv("MARKETSTACK_API_KEY"), limit=1
    )
    assert response.pagination.count == 1
    assert response.data[0].symbol == "$"
    assert response.data[0].code == "USD"
