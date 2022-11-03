import os
from datetime import datetime

from marketstack.api.intraday import intraday, intraday_date, intraday_latest
from marketstack.client import Client

from tests.setup import create_client, date_from, date_to

client: Client


def setup_module():
    global client
    client = create_client()


def test_intraday():
    response = intraday.sync(
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbols="AAPL,AMZN",
        date_from=date_from,
        date_to=date_to,
        interval="1hour",
        limit=10,
    )
    aapl = None
    amzn = None
    for price in response.data:
        if price.symbol == "AAPL":
            aapl = price
        elif price.symbol == "AMZN":
            amzn = price

    assert response.pagination.offset == 0
    assert response.pagination.limit == 10
    assert response.pagination.count == 10

    for price in [aapl, amzn]:
        assert price.open_ > 0
        assert len(price.exchange) > 0
        assert isinstance(price.date, datetime)
        assert price.low > 0
        assert price.high > 0


def test_intraday_latest():
    response = intraday_latest.sync(
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        symbols="AAPL",
    )
    assert response.pagination.count == 1
    assert response.data[0].symbol == "AAPL"


def test_intraday_date():
    response = intraday_date.sync(
        symbols="AAPL",
        date=date_from,
        client=client,
        access_key=os.getenv("MARKETSTACK_API_KEY"),
        limit=1,
    )
    assert response.pagination.count == 1
    assert response.pagination.limit == 1
    assert response.pagination.total > 0
    assert response.data[0].symbol == "AAPL"
    assert response.data[0].open_ > 0
