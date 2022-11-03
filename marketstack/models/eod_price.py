import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EodPrice")


@attr.s(auto_attribs=True)
class EodPrice:
    """
    Attributes:
        date (datetime.datetime):
        symbol (str):
        open_ (float):
        low (float):
        high (float):
        exchange (str):
        split_factor (float):
        dividend (float):
        adj_open (float):
        adj_close (float):
        adj_high (float):
        adj_low (float):
        adj_volume (float):
        volume (Union[Unset, float]):
        close (Union[Unset, float]):
        last (Union[Unset, float]):
    """

    date: datetime.datetime
    symbol: str
    open_: float
    low: float
    high: float
    exchange: str
    split_factor: float
    dividend: float
    adj_open: float
    adj_close: float
    adj_high: float
    adj_low: float
    adj_volume: float
    volume: Union[Unset, float] = UNSET
    close: Union[Unset, float] = UNSET
    last: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date = self.date.isoformat()

        symbol = self.symbol
        open_ = self.open_
        low = self.low
        high = self.high
        exchange = self.exchange
        split_factor = self.split_factor
        dividend = self.dividend
        adj_open = self.adj_open
        adj_close = self.adj_close
        adj_high = self.adj_high
        adj_low = self.adj_low
        adj_volume = self.adj_volume
        volume = self.volume
        close = self.close
        last = self.last

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "symbol": symbol,
                "open": open_,
                "low": low,
                "high": high,
                "exchange": exchange,
                "split_factor": split_factor,
                "dividend": dividend,
                "adj_open": adj_open,
                "adj_close": adj_close,
                "adj_high": adj_high,
                "adj_low": adj_low,
                "adj_volume": adj_volume,
            }
        )
        if volume is not UNSET:
            field_dict["volume"] = volume
        if close is not UNSET:
            field_dict["close"] = close
        if last is not UNSET:
            field_dict["last"] = last

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date = isoparse(d.pop("date"))

        symbol = d.pop("symbol")

        open_ = d.pop("open")

        low = d.pop("low")

        high = d.pop("high")

        exchange = d.pop("exchange")

        split_factor = d.pop("split_factor")

        dividend = d.pop("dividend")

        adj_open = d.pop("adj_open")

        adj_close = d.pop("adj_close")

        adj_high = d.pop("adj_high")

        adj_low = d.pop("adj_low")

        adj_volume = d.pop("adj_volume")

        volume = d.pop("volume", UNSET)

        close = d.pop("close", UNSET)

        last = d.pop("last", UNSET)

        eod_price = cls(
            date=date,
            symbol=symbol,
            open_=open_,
            low=low,
            high=high,
            exchange=exchange,
            split_factor=split_factor,
            dividend=dividend,
            adj_open=adj_open,
            adj_close=adj_close,
            adj_high=adj_high,
            adj_low=adj_low,
            adj_volume=adj_volume,
            volume=volume,
            close=close,
            last=last,
        )

        eod_price.additional_properties = d
        return eod_price

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
