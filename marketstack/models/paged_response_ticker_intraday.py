from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.pagination import Pagination
from ..models.ticker_intraday import TickerIntraday

T = TypeVar("T", bound="PagedResponseTickerIntraday")


@attr.s(auto_attribs=True)
class PagedResponseTickerIntraday:
    """
    Attributes:
        pagination (Pagination):
        data (TickerIntraday):
    """

    pagination: Pagination
    data: TickerIntraday
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pagination = self.pagination.to_dict()

        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination": pagination,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pagination = Pagination.from_dict(d.pop("pagination"))

        data = TickerIntraday.from_dict(d.pop("data"))

        paged_response_ticker_intraday = cls(
            pagination=pagination,
            data=data,
        )

        paged_response_ticker_intraday.additional_properties = d
        return paged_response_ticker_intraday

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
