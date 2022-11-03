import os

from marketstack.api.eod import eod, eod_date, eod_latest
from marketstack.client import Client
from tests.setup import create_client, this_january, this_february, day_format

client: Client


def setup_module():
    global client
    client = create_client()


def test_eod():
    response = eod.sync(
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbols="AAPL,AMZN",
        date_from=this_january,
        date_to=this_february,
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

    for price in [aapl, amzn]:
        assert price.open_ > 0
        assert len(price.exchange) > 0


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
        date=this_january,
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        limit=1,
    )
    assert response.pagination.count == 1
    assert response.pagination.limit == 1
    assert response.pagination.total == 1
    assert response.data[0].symbol == "AAPL"
    assert response.data[0].open_ > 0
    assert response.data[0].date.strftime(day_format) == this_january
