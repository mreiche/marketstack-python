import os

from marketstack.api.eod import eod, eod_latest, eod_date
from marketstack.client import Client
from tests.setup import create_client, date_from, date_to

client: Client


def setup_module():
    global client
    client = create_client()


def test_eod():
    response = eod.sync(
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbols="AAPL,AMZN",
        date_from=date_from,
        date_to=date_to,
        limit=10,
    )
    aapl = None
    amzn = None
    for price in response.data:
        if price.symbol == "AAPL":
            aapl = price
        elif price.symbol == "AMZN":
            amzn = price

    assert response.pagination.limit == 10
    assert response.pagination.count == 10
    assert aapl.open_ > 0
    assert len(amzn.exchange) > 0
    assert amzn.open_ > 0
    assert len(amzn.exchange) > 0


def test_eod_latest():
    response = eod_latest.sync(
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbols="AAPL",
    )
    assert response.pagination.count == 1
    assert response.data[0].symbol == "AAPL"


def test_eod_date():
    response = eod_date.sync(
        symbols="AAPL",
        date=date_from,
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        limit=1
    )
    assert response.pagination.count == 1
    assert response.pagination.limit == 1
    assert response.pagination.total == 1
    assert response.data[0].symbol == "AAPL"
    assert response.data[0].open_ > 0
