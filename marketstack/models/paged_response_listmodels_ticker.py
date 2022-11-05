from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.pagination import Pagination
from ..models.ticker import Ticker

T = TypeVar("T", bound="PagedResponseListmodelsTicker")


@attr.s(auto_attribs=True)
class PagedResponseListmodelsTicker:
    """
    Attributes:
        pagination (Pagination):
        data (List[Ticker]):
    """

    pagination: Pagination
    data: List[Ticker]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pagination = self.pagination.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()

            data.append(data_item)

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

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = Ticker.from_dict(data_item_data)

            data.append(data_item)

        paged_response_listmodels_ticker = cls(
            pagination=pagination,
            data=data,
        )

        paged_response_listmodels_ticker.additional_properties = d
        return paged_response_listmodels_ticker

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
