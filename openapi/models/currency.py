from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Currency")


@attr.s(auto_attribs=True)
class Currency:
    """
    Attributes:
        code (str):
        name (str):
        symbol (Union[Unset, str]):
        symbol_native (Union[Unset, str]):
    """

    code: str
    name: str
    symbol: Union[Unset, str] = UNSET
    symbol_native: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        name = self.name
        symbol = self.symbol
        symbol_native = self.symbol_native

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "name": name,
            }
        )
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if symbol_native is not UNSET:
            field_dict["symbol_native"] = symbol_native

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code")

        name = d.pop("name")

        symbol = d.pop("symbol", UNSET)

        symbol_native = d.pop("symbol_native", UNSET)

        currency = cls(
            code=code,
            name=name,
            symbol=symbol,
            symbol_native=symbol_native,
        )

        currency.additional_properties = d
        return currency

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
