from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.error_code import ErrorCode
from ..models.error_context import ErrorContext
from ..types import UNSET, Unset

T = TypeVar("T", bound="Error")


@attr.s(auto_attribs=True)
class Error:
    """
    Attributes:
        code (ErrorCode): An enumeration.
        message (str):
        context (Union[Unset, ErrorContext]):
    """

    code: ErrorCode
    message: str
    context: Union[Unset, ErrorContext] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code.value

        message = self.message
        context: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = ErrorCode(d.pop("code"))

        message = d.pop("message")

        _context = d.pop("context", UNSET)
        context: Union[Unset, ErrorContext]
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = ErrorContext.from_dict(_context)

        error = cls(
            code=code,
            message=message,
            context=context,
        )

        error.additional_properties = d
        return error

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
