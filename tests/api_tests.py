from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from marketstack import query_intraday, Interval, ErrorCode, query_eod, IntradayRequest, EodRequest, query_splits, SplitsRequest, PathComponent, query_dividends, DividendsRequest, query_currencies, CurrenciesRequest, query_timezones, TimezonesRequest, query_tickers, TickersRequest, query_exchanges, ExchangesRequest

date_format = "%Y-%m-%d %H:%M:%S"


def setup_module():
    assert load_dotenv(Path(__file__).parent / "test.env") is True


def test_query_intraday_feature_not_supported():
    response = query_intraday(
        IntradayRequest(
            symbols=["AAPL", "AMZN"],
            interval=Interval.min5,
        )
    )
    assert response.error.code == ErrorCode.function_access_restricted


def test_query_intraday_symbols():
    response = query_intraday(
        IntradayRequest(
            symbols=["AAPL", "AMZN"],
            limit=10,
            date_from=datetime.strptime("2022-01-01 00:00:00", date_format),
            date_to=datetime.strptime("2022-01-01 23:23:59", date_format),
        )
    )
    assert response.error is None
    aapl = None
    amzn = None
    for price in response.data:
        if price.symbol == "AAPL":
            aapl = price
        elif price.symbol == "AMZN":
            amzn = price

    assert response.pagination.limit == 10
    assert response.pagination.count == 6
    assert aapl.open > 0
    assert aapl.exchange == "IEXG"
    assert amzn.open > 0
    assert amzn.exchange == "IEXG"
    assert aapl.date.isoformat() == "2022-01-01T00:00:00+00:00"


def test_query_intraday_symbols_specific_date():
    reference_date = datetime.strptime("2022-01-01 00:00:00", date_format)
    response = query_intraday(IntradayRequest(symbols=["AAPL"], date=reference_date))
    assert response.error is None
    assert response.pagination.count == 1
    aapl = response.data[0]
    assert aapl.date.isoformat() == "2022-01-01T00:00:00+00:00"


def test_query_intraday_symbols_latest():
    response = query_intraday(IntradayRequest(symbols=["AAPL"], date=PathComponent.latest))
    assert response.error is None
    assert response.pagination.count == 1


def test_query_eod():
    response = query_eod(EodRequest(symbols=["AAPL"], date=PathComponent.latest))
    assert response.error is None
    assert response.pagination.count == 1
    assert response.data[0].adj_low > 0


def test_query_splits():
    reference_date = datetime.strptime("2022-01-01 00:00:00", date_format)
    response = query_splits(SplitsRequest(symbols=["AAPL"], date_to=reference_date))
    assert response.error is None
    assert response.pagination.count == 5
    assert response.data[0].datetime.isoformat() == "2020-08-31T00:00:00"
    assert response.data[0].split_factor > 0
    assert response.data[0].symbol == "AAPL"


def test_query_dividends():
    response = query_dividends(
        DividendsRequest(
            symbols=["AAPL"],
            date_from=datetime.strptime("2020-01-01 00:00:00", date_format),
            date_to=datetime.strptime("2020-12-31 00:00:00", date_format),
        )
    )
    assert response.error is None
    assert response.pagination.count == 4
    assert response.data[0].datetime.isoformat() == "2020-11-06T00:00:00"
    assert response.data[0].dividend > 0
    assert response.data[0].symbol == "AAPL"


def test_query_currencies():
    response = query_currencies(CurrenciesRequest(limit=1))
    assert response.error is None
    assert response.pagination.count == 1
    assert response.data[0].symbol == "$"
    assert response.data[0].code == "USD"


def test_query_timezones():
    response = query_timezones(TimezonesRequest(limit=1))
    assert response.error is None
    assert response.pagination.count == 1
    assert response.data[0].timezone == "America/New_York"


def test_query_tickers():
    response = query_tickers(TickersRequest(limit=1))
    assert response.error is None
    assert response.pagination.count == 1
    assert response.data[0].symbol == "MSFT"


def test_query_exchanges():
    response = query_exchanges(ExchangesRequest(limit=1))
    assert response.error is None
    assert response.pagination.count == 1
    assert response.data[0].mic == "XNAS"
