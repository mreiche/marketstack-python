import os

from marketstack.api.splits import splits
from marketstack.client import Client
from marketstack.models import ErrorResponse
from tests.setup import create_client, last_january, last_december

client: Client


def setup_module():
    global client
    client = create_client()


def test_splits():
    response = splits.sync(
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbols="AAPL",
        date_from=last_january,
        date_to=last_december,
    )

    # We don't know if splits happend
    assert isinstance(response, ErrorResponse) is False
