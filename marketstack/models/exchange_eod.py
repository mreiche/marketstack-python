from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.currency import Currency
from ..models.eod_price import EodPrice
from ..models.timezone import Timezone
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExchangeEod")


@attr.s(auto_attribs=True)
class ExchangeEod:
    """
    Attributes:
        name (str):
        acronym (str):
        mic (str):
        country (str):
        city (str):
        website (str):
        eod (List[EodPrice]):
        country_code (Union[Unset, str]):
        currency (Union[Unset, Currency]):
        timezone (Union[Unset, Timezone]):
    """

    name: str
    acronym: str
    mic: str
    country: str
    city: str
    website: str
    eod: List[EodPrice]
    country_code: Union[Unset, str] = UNSET
    currency: Union[Unset, Currency] = UNSET
    timezone: Union[Unset, Timezone] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        acronym = self.acronym
        mic = self.mic
        country = self.country
        city = self.city
        website = self.website
        eod = []
        for eod_item_data in self.eod:
            eod_item = eod_item_data.to_dict()

            eod.append(eod_item)

        country_code = self.country_code
        currency: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.to_dict()

        timezone: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.timezone, Unset):
            timezone = self.timezone.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "acronym": acronym,
                "mic": mic,
                "country": country,
                "city": city,
                "website": website,
                "eod": eod,
            }
        )
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
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

        city = d.pop("city")

        website = d.pop("website")

        eod = []
        _eod = d.pop("eod")
        for eod_item_data in _eod:
            eod_item = EodPrice.from_dict(eod_item_data)

            eod.append(eod_item)

        country_code = d.pop("country_code", UNSET)

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, Currency]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = Currency.from_dict(_currency)

        _timezone = d.pop("timezone", UNSET)
        timezone: Union[Unset, Timezone]
        if isinstance(_timezone, Unset):
            timezone = UNSET
        else:
            timezone = Timezone.from_dict(_timezone)

        exchange_eod = cls(
            name=name,
            acronym=acronym,
            mic=mic,
            country=country,
            city=city,
            website=website,
            eod=eod,
            country_code=country_code,
            currency=currency,
            timezone=timezone,
        )

        exchange_eod.additional_properties = d
        return exchange_eod

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
