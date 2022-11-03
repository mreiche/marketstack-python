import asyncio
import os

from marketstack.api.timezones import timezones
from marketstack.client import Client
from tests.setup import create_client

client: Client


def setup_module():
    global client
    client = create_client()


def test_timezones():
    response = timezones.sync(
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        limit=1
    )
    assert response.pagination.count == 1
    assert response.data[0].timezone == "America/New_York"
