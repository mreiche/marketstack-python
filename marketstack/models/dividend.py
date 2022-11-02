from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="Dividend")


@attr.s(auto_attribs=True)
class Dividend:
    """
    Attributes:
        date (str):
        symbol (str):
        dividend (float):
    """

    date: str
    symbol: str
    dividend: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date = self.date
        symbol = self.symbol
        dividend = self.dividend

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "symbol": symbol,
                "dividend": dividend,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date = d.pop("date")

        symbol = d.pop("symbol")

        dividend = d.pop("dividend")

        dividend = cls(
            date=date,
            symbol=symbol,
            dividend=dividend,
        )

        dividend.additional_properties = d
        return dividend

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
