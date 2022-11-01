import os
from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import List, TypeVar, Generic, Literal

import requests
from pydantic import BaseModel
from pydantic.generics import GenericModel

__version__ = 'dev'

R = TypeVar('R')


def __format_datetime(date: datetime | str):
    if isinstance(date, datetime):
        return date.isoformat() + 'Z'
    return date


def __build_request(request: object | None, exclude_params: List[str] = []):
    tls_support = os.getenv("MARKETSTACK_TLS_SUPPORT")
    access_key = os.getenv("MARKETSTACK_API_KEY")
    assert access_key is not None and len(
        access_key
    ) > 0, "Environment variable MARKETSTACK_API_KEY is not defined"

    params = {}
    if request:
        for param, val in request.__dict__.items():
            if val is None or param in exclude_params:
                continue
            params[param] = val

    params['access_key'] = access_key
    protocol = "https" if tls_support == "1" else "http"
    return f"{protocol}://api.marketstack.com/v1", params


class Pagination(BaseModel):
    limit: int
    offset: int
    count: int
    total: int


class ErrorCode(StrEnum):
    invalid_access_key = "invalid_access_key"
    missing_access_key = "missing_access_key"
    function_access_restricted = "function_access_restricted"
    inactive_user = "inactive_user"
    https_access_restricted = "https_access_restricted"
    invalid_api_function = "invalid_api_function"
    not_found = "404_not_found"
    usage_limit_reached = "usage_limit_reached"
    rate_limit_reached = "rate_limit_reached"
    internal_error = "internal_error"
    validation_error = "validation_error"


class Error(BaseModel):
    code: ErrorCode
    message: str
    context: dict | None


class Response(GenericModel, Generic[R]):
    pagination: Pagination | None
    data: List[R] | None
    error: Error | None


class SimpleDate(BaseModel):
    date: str

    @property
    def datetime(self):
        return datetime.strptime(self.date, "%Y-%m-%d")


class Split(SimpleDate):
    symbol: str
    split_factor: float


class Dividend(SimpleDate):
    symbol: str
    dividend: float


class IntervalPrice(BaseModel):
    date: datetime
    symbol: str
    volume: float|None
    open: float
    close: float | None
    low: float
    high: float
    exchange: str


class EodPrice(IntervalPrice):
    split_factor: float
    dividend: float
    adj_open: float
    adj_close: float
    adj_high: float
    adj_low: float
    adj_volume: float


class Interval(StrEnum):
    min1 = "1min"
    min5 = "5min"
    min10 = "10min"
    min30 = "30min"
    hour1 = "1hour"
    hour3 = "3hour"
    hour6 = "6hour"
    hour12 = "12hour"
    hour24 = "24hour"


class Sort(StrEnum):
    ASC = "ASC"
    DESC = "DESC"


@dataclass()
class SymbolsRequest:
    symbols: List[str]
    sort: Sort = None
    date_from: datetime = None
    date_to: datetime = None
    limit: int = None
    offset: int = None

    def get_symbols(self):
        return ",".join(map(str.strip, self.symbols))


@dataclass()
class DateRequest(SymbolsRequest):
    date: datetime | Literal["latest"] = None


@dataclass()
class EodRequest(DateRequest):
    exchange: str = None


@dataclass()
class IntradayRequest(EodRequest):
    interval: Interval = None


@dataclass()
class SplitsRequest(SymbolsRequest):
    pass


@dataclass()
class DividendsRequest(SymbolsRequest):
    pass


@dataclass()
class TickersRequest:
    symbol: str
    search: str = None
    exchange: str = None
    limit: int = None
    offset: int = None


@dataclass()
class ExchangesRequest:
    search: str = None
    limit: int = None
    offset: int = None


@dataclass()
class CurrenciesRequest:
    limit: int = None
    offset: int = None


@dataclass()
class TimezonesRequest:
    limit: int = None
    offset: int = None


class Currency(BaseModel):
    code: str
    name: str
    symbol: str | None
    symbol_native: str | None


class Timezone(BaseModel):
    timezone: str
    abbr: str
    abbr_dst: str


class Exchange(BaseModel):
    name: str
    acronym: str
    mic: str
    country: str
    country_code: str
    city: str
    website: str
    timezone: Timezone


class Ticker(BaseModel):
    name: str
    symbol: str
    stock_exchange: Exchange


def __date_query(
    endpoint: str,
    request: DateRequest,
    response_type: R,
):
    base_url, params = __build_request(request, exclude_params=["date"])
    #params["symbols"] = request.get_symbols()

    url = f"{base_url}/{endpoint}"
    if request.date:
        url += f"/{__format_datetime(request.date)}"

    result = requests.get(url, params)
    return Response[response_type](**result.json())


def __simple_query(
    endpoint: str,
    request: object | None,
    response_type: R,
):
    base_url, params = __build_request(request)
    url = f"{base_url}/{endpoint}"
    result = requests.get(url, params)
    return Response[response_type](**result.json())


def query_intraday(request: IntradayRequest) -> Response[IntervalPrice]:
    return __date_query("intraday", request, IntervalPrice)


def query_eod(request: EodRequest) -> Response[EodPrice]:
    return __date_query("eod", request, EodPrice)


def query_splits(request: SplitsRequest) -> Response[Split]:
    return __simple_query("splits", request, Split)


def query_dividends(request: DividendsRequest) -> Response[Dividend]:
    return __simple_query("dividends", request, Dividend)


def query_currencies(request: CurrenciesRequest = None) -> Response[Currency]:
    return __simple_query("currencies", request, Currency)


def query_timezones(request: TimezonesRequest = None) -> Response[Timezone]:
    return __simple_query("timezones", request, Timezone)


def query_tickers(request: TickersRequest = None) -> Response[Ticker]:
    return __simple_query("tickers", request, Ticker)


def query_exchanges(request: ExchangesRequest = None) -> Response[Exchange]:
    return __simple_query("exchanges", request, Exchange)
