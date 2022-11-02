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


class PathComponent(StrEnum):
    tickers = "tickers"
    exchanges = "exchanges"
    eod = "eod"
    intraday = "intraday"
    latest = "latest"
    splits = "splits"
    dividends = "dividends"
    currencies = "currencies"


class BaseRequest:
    def get_query_params(self, exclude_params: List[str] = None) -> dict[str, str]:
        params = {}
        for param, val in self.__dict__.items():
            if val is None or param in exclude_params:
                continue
            params[param] = val
        return params

    def get_path_params(self) -> List[str]:
        return []

    def get_response_type(self) -> R:
        return None


def __build_request(request: BaseRequest | None):
    tls_support = os.getenv("MARKETSTACK_TLS_SUPPORT")
    access_key = os.getenv("MARKETSTACK_API_KEY")
    assert access_key is not None and len(
        access_key
    ) > 0, "Environment variable MARKETSTACK_API_KEY is not defined"

    query_params = request.get_query_params()
    query_params['access_key'] = access_key
    protocol = "https" if tls_support == "1" else "http"
    return f"{protocol}://api.marketstack.com/v1/" + ("/".join(request.get_path_params())), query_params


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
    volume: float | None
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
class SymbolsRequest(BaseRequest):
    symbols: List[str]
    sort: Sort = None
    date_from: datetime = None
    date_to: datetime = None
    limit: int = None
    offset: int = None

    def get_query_params(self, **kwargs):
        params = super().get_query_params(exclude_params=["symbols"])
        params['symbols'] = ",".join(map(str.strip, self.symbols))
        return params


@dataclass()
class EodRequest(SymbolsRequest):
    exchange: str = None
    date: datetime | Literal[PathComponent.latest] = None

    def get_path_params(self) -> List[str]:
        path = [PathComponent.eod]
        if self.date is not None:
            path.append(__format_datetime(self.date))
        return path


@dataclass()
class IntradayRequest(SymbolsRequest):
    interval: Interval = None
    exchange: str = None
    date: datetime|Literal[PathComponent.latest] = None

    def get_path_params(self) -> List[str]:
        path = [PathComponent.intraday]
        if self.date is not None:
            path.append(__format_datetime(self.date))
        return path


@dataclass()
class SplitsRequest(SymbolsRequest):
    def get_path_params(self) -> List[str]:
        return [PathComponent.splits]


@dataclass()
class DividendsRequest(SymbolsRequest):
    def get_path_params(self) -> List[str]:
        return [PathComponent.dividends]

    def get_response_type(self) -> R:
        return Dividend


@dataclass()
class TickersRequest(BaseRequest):
    symbol: str = None
    search: str = None
    exchange: str = None
    limit: int = None
    offset: int = None
    date: datetime|Literal[PathComponent.latest] = None
    subpath: PathComponent = None

    def get_path_params(self):
        path = [PathComponent.tickers]
        if self.symbol is not None:
            path.append(self.symbol)
            if self.subpath is not None:
                path.append(self.subpath)
                if self.date is not None:
                    path.append(__format_datetime(self.date))


@dataclass()
class ExchangesRequest(BaseRequest):
    search: str = None
    limit: int = None
    offset: int = None
    subpath: PathComponent = None
    mic: str = None
    date: datetime|Literal[PathComponent.latest] = None

    def get_path_params(self):
        # "{Company} is a {Department} Portal.".format(**value)
        path = [PathComponent.exchanges]
        if self.mic is not None:
            path.append(self.mic)
            if self.subpath is not None:
                path.append(self.subpath)
                if self.date is not None:
                    path.append(__format_datetime(self.date))


@dataclass()
class CurrenciesRequest(BaseRequest):
    limit: int = None
    offset: int = None

    def get_path_params(self):
        return [PathComponent.currencies]


@dataclass()
class TimezonesRequest(BaseRequest):
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


def __query(request: BaseRequest, response_type: R):
    url, params = __build_request(request)
    result = requests.get(url, params)
    return Response[response_type](**result.json())


def query_intraday(request: IntradayRequest) -> Response[IntervalPrice]:
    return __query(request, IntervalPrice)


def query_eod(request: EodRequest) -> Response[EodPrice]:
    return __query(request, EodPrice)


def query_splits(request: SplitsRequest) -> Response[Split]:
    return __query(request, Split)


def query_dividends(request: DividendsRequest) -> Response[Dividend]:
    return __query(request, Dividend)


def query_currencies(request: CurrenciesRequest = None) -> Response[Currency]:
    return __query(request, Currency)


def query_timezones(request: TimezonesRequest = None) -> Response[Timezone]:
    return __query(request, Timezone)


def query_tickers(request: TickersRequest = None) -> Response[Ticker]:
    return __query(request, Ticker)


def query_exchanges(request: ExchangesRequest = None) -> Response[Exchange]:
    return __query(request, Exchange)
