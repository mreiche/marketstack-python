from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="Timezone")


@attr.s(auto_attribs=True)
class Timezone:
    """
    Attributes:
        timezone (str):
        abbr (str):
        abbr_dst (str):
    """

    timezone: str
    abbr: str
    abbr_dst: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timezone = self.timezone
        abbr = self.abbr
        abbr_dst = self.abbr_dst

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timezone": timezone,
                "abbr": abbr,
                "abbr_dst": abbr_dst,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timezone = d.pop("timezone")

        abbr = d.pop("abbr")

        abbr_dst = d.pop("abbr_dst")

        timezone = cls(
            timezone=timezone,
            abbr=abbr,
            abbr_dst=abbr_dst,
        )

        timezone.additional_properties = d
        return timezone

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
