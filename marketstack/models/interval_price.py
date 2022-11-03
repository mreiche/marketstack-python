import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="IntervalPrice")


@attr.s(auto_attribs=True)
class IntervalPrice:
    """
    Attributes:
        date (datetime.datetime):
        symbol (str):
        open_ (float):
        low (float):
        high (float):
        exchange (str):
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

        volume = d.pop("volume", UNSET)

        close = d.pop("close", UNSET)

        last = d.pop("last", UNSET)

        interval_price = cls(
            date=date,
            symbol=symbol,
            open_=open_,
            low=low,
            high=high,
            exchange=exchange,
            volume=volume,
            close=close,
            last=last,
        )

        interval_price.additional_properties = d
        return interval_price

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
