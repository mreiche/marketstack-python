from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.eod_price import EodPrice
from ..models.interval_price import IntervalPrice
from ..types import UNSET, Unset

T = TypeVar("T", bound="TickerSymbol")


@attr.s(auto_attribs=True)
class TickerSymbol:
    """
    Attributes:
        name (str):
        symbol (str):
        has_intraday (bool):
        has_eod (bool):
        coountry (Union[Unset, str]):
        eod (Union[Unset, List[EodPrice]]):
        intraday (Union[Unset, List[IntervalPrice]]):
    """

    name: str
    symbol: str
    has_intraday: bool
    has_eod: bool
    coountry: Union[Unset, str] = UNSET
    eod: Union[Unset, List[EodPrice]] = UNSET
    intraday: Union[Unset, List[IntervalPrice]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        symbol = self.symbol
        has_intraday = self.has_intraday
        has_eod = self.has_eod
        coountry = self.coountry
        eod: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.eod, Unset):
            eod = []
            for eod_item_data in self.eod:
                eod_item = eod_item_data.to_dict()

                eod.append(eod_item)

        intraday: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.intraday, Unset):
            intraday = []
            for intraday_item_data in self.intraday:
                intraday_item = intraday_item_data.to_dict()

                intraday.append(intraday_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "symbol": symbol,
                "has_intraday": has_intraday,
                "has_eod": has_eod,
            }
        )
        if coountry is not UNSET:
            field_dict["coountry"] = coountry
        if eod is not UNSET:
            field_dict["eod"] = eod
        if intraday is not UNSET:
            field_dict["intraday"] = intraday

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        symbol = d.pop("symbol")

        has_intraday = d.pop("has_intraday")

        has_eod = d.pop("has_eod")

        coountry = d.pop("coountry", UNSET)

        eod = []
        _eod = d.pop("eod", UNSET)
        for eod_item_data in _eod or []:
            eod_item = EodPrice.from_dict(eod_item_data)

            eod.append(eod_item)

        intraday = []
        _intraday = d.pop("intraday", UNSET)
        for intraday_item_data in _intraday or []:
            intraday_item = IntervalPrice.from_dict(intraday_item_data)

            intraday.append(intraday_item)

        ticker_symbol = cls(
            name=name,
            symbol=symbol,
            has_intraday=has_intraday,
            has_eod=has_eod,
            coountry=coountry,
            eod=eod,
            intraday=intraday,
        )

        ticker_symbol.additional_properties = d
        return ticker_symbol

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
