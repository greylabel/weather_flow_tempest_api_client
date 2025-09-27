from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="BetterForecastDailyForecast")



@_attrs_define
class BetterForecastDailyForecast:
    """ 
        Attributes:
            day_start_local (Union[Unset, float]):  Example: 1608699600.
            day_num (Union[Unset, float]):  Example: 23.
            month_num (Union[Unset, float]):  Example: 12.
            conditions (Union[Unset, str]):  Example: Clear.
            icon (Union[Unset, str]):  Example: clear-day.
            sunrise (Union[Unset, float]):  Example: 1608639322.
            sunset (Union[Unset, float]):  Example: 1608676362.
            air_temp_high (Union[Unset, float]):  Example: 73.
            air_temp_low (Union[Unset, float]):  Example: 39.
            precip_probability (Union[Unset, float]):  Example: 10.
            precip_icon (Union[Unset, str]):  Example: chance-rain.
            precip_type (Union[Unset, str]):  Example: rain.
     """

    day_start_local: Union[Unset, float] = UNSET
    day_num: Union[Unset, float] = UNSET
    month_num: Union[Unset, float] = UNSET
    conditions: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    sunrise: Union[Unset, float] = UNSET
    sunset: Union[Unset, float] = UNSET
    air_temp_high: Union[Unset, float] = UNSET
    air_temp_low: Union[Unset, float] = UNSET
    precip_probability: Union[Unset, float] = UNSET
    precip_icon: Union[Unset, str] = UNSET
    precip_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        day_start_local = self.day_start_local

        day_num = self.day_num

        month_num = self.month_num

        conditions = self.conditions

        icon = self.icon

        sunrise = self.sunrise

        sunset = self.sunset

        air_temp_high = self.air_temp_high

        air_temp_low = self.air_temp_low

        precip_probability = self.precip_probability

        precip_icon = self.precip_icon

        precip_type = self.precip_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if day_start_local is not UNSET:
            field_dict["day_start_local"] = day_start_local
        if day_num is not UNSET:
            field_dict["day_num"] = day_num
        if month_num is not UNSET:
            field_dict["month_num"] = month_num
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if icon is not UNSET:
            field_dict["icon"] = icon
        if sunrise is not UNSET:
            field_dict["sunrise"] = sunrise
        if sunset is not UNSET:
            field_dict["sunset"] = sunset
        if air_temp_high is not UNSET:
            field_dict["air_temp_high"] = air_temp_high
        if air_temp_low is not UNSET:
            field_dict["air_temp_low"] = air_temp_low
        if precip_probability is not UNSET:
            field_dict["precip_probability"] = precip_probability
        if precip_icon is not UNSET:
            field_dict["precip_icon"] = precip_icon
        if precip_type is not UNSET:
            field_dict["precip_type"] = precip_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        day_start_local = d.pop("day_start_local", UNSET)

        day_num = d.pop("day_num", UNSET)

        month_num = d.pop("month_num", UNSET)

        conditions = d.pop("conditions", UNSET)

        icon = d.pop("icon", UNSET)

        sunrise = d.pop("sunrise", UNSET)

        sunset = d.pop("sunset", UNSET)

        air_temp_high = d.pop("air_temp_high", UNSET)

        air_temp_low = d.pop("air_temp_low", UNSET)

        precip_probability = d.pop("precip_probability", UNSET)

        precip_icon = d.pop("precip_icon", UNSET)

        precip_type = d.pop("precip_type", UNSET)

        better_forecast_daily_forecast = cls(
            day_start_local=day_start_local,
            day_num=day_num,
            month_num=month_num,
            conditions=conditions,
            icon=icon,
            sunrise=sunrise,
            sunset=sunset,
            air_temp_high=air_temp_high,
            air_temp_low=air_temp_low,
            precip_probability=precip_probability,
            precip_icon=precip_icon,
            precip_type=precip_type,
        )


        better_forecast_daily_forecast.additional_properties = d
        return better_forecast_daily_forecast

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
