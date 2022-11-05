from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.currency import Currency
from ..models.timezone import Timezone
from ..types import UNSET, Unset

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
        currency (Union[Currency, None, Unset]):
        timezone (Union[None, Timezone, Unset]):
    """

    name: str
    acronym: str
    mic: str
    country: str
    country_code: str
    city: str
    website: str
    currency: Union[Currency, None, Unset] = UNSET
    timezone: Union[None, Timezone, Unset] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        acronym = self.acronym
        mic = self.mic
        country = self.country
        country_code = self.country_code
        city = self.city
        website = self.website
        currency: Union[Dict[str, Any], None, Unset]
        if isinstance(self.currency, Unset):
            currency = UNSET

        elif isinstance(self.currency, Currency):
            currency = UNSET
            if not isinstance(self.currency, Unset):
                currency = self.currency.to_dict()

        else:
            currency = self.currency

        timezone: Union[Dict[str, Any], None, Unset]
        if isinstance(self.timezone, Unset):
            timezone = UNSET

        elif isinstance(self.timezone, Timezone):
            timezone = UNSET
            if not isinstance(self.timezone, Unset):
                timezone = self.timezone.to_dict()

        else:
            timezone = self.timezone

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
        if currency is not UNSET:
            field_dict["currency"] = currency
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

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

        def _parse_currency(data: object) -> Union[Currency, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _currency_type_0 = data
                currency_type_0: Union[Unset, Currency]
                if isinstance(_currency_type_0, Unset):
                    currency_type_0 = UNSET
                else:
                    currency_type_0 = Currency.from_dict(_currency_type_0)

                return currency_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Currency, None, Unset], data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_timezone(data: object) -> Union[None, Timezone, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _timezone_type_0 = data
                timezone_type_0: Union[Unset, Timezone]
                if isinstance(_timezone_type_0, Unset):
                    timezone_type_0 = UNSET
                else:
                    timezone_type_0 = Timezone.from_dict(_timezone_type_0)

                return timezone_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Timezone, Unset], data)

        timezone = _parse_timezone(d.pop("timezone", UNSET))

        exchange = cls(
            name=name,
            acronym=acronym,
            mic=mic,
            country=country,
            country_code=country_code,
            city=city,
            website=website,
            currency=currency,
            timezone=timezone,
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
