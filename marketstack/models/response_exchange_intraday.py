from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.error import Error
from ..models.exchange_intraday import ExchangeIntraday
from ..models.pagination import Pagination
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResponseExchangeIntraday")


@attr.s(auto_attribs=True)
class ResponseExchangeIntraday:
    """
    Attributes:
        pagination (Union[Unset, Pagination]):
        data (Union[Unset, ExchangeIntraday]):
        error (Union[Unset, Error]):
    """

    pagination: Union[Unset, Pagination] = UNSET
    data: Union[Unset, ExchangeIntraday] = UNSET
    error: Union[Unset, Error] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pagination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if data is not UNSET:
            field_dict["data"] = data
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        _data = d.pop("data", UNSET)
        data: Union[Unset, ExchangeIntraday]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ExchangeIntraday.from_dict(_data)

        _error = d.pop("error", UNSET)
        error: Union[Unset, Error]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = Error.from_dict(_error)

        response_exchange_intraday = cls(
            pagination=pagination,
            data=data,
            error=error,
        )

        response_exchange_intraday.additional_properties = d
        return response_exchange_intraday

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
