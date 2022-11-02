from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="Exchange")


@attr.s(auto_attribs=True)
class Exchange:
    """
    Attributes:
        name (str):
        acronym (str):
        mic (str):
        country (str):
        country_code (str):
        city (str):
        website (str):
    """

    name: str
    acronym: str
    mic: str
    country: str
    country_code: str
    city: str
    website: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        acronym = self.acronym
        mic = self.mic
        country = self.country
        country_code = self.country_code
        city = self.city
        website = self.website

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "acronym": acronym,
                "mic": mic,
                "country": country,
                "country_code": country_code,
                "city": city,
                "website": website,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        acronym = d.pop("acronym")

        mic = d.pop("mic")

        country = d.pop("country")

        country_code = d.pop("country_code")

        city = d.pop("city")

        website = d.pop("website")

        exchange = cls(
            name=name,
            acronym=acronym,
            mic=mic,
            country=country,
            country_code=country_code,
            city=city,
            website=website,
        )

        exchange.additional_properties = d
        return exchange

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
