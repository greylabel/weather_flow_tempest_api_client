from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="BetterForecastHourlyForecast")



@_attrs_define
class BetterForecastHourlyForecast:
    """ 
        Attributes:
            time (Union[Unset, float]):  Example: 1608735600.
            conditions (Union[Unset, str]):  Example: Clear.
            icon (Union[Unset, str]):  Example: clear-day.
            air_temperature (Union[Unset, float]):  Example: 57.
            sea_level_pressure (Union[Unset, float]):  Example: 30.257.
            relative_humidity (Union[Unset, float]):  Example: 82.
            precip (Union[Unset, float]):
            precip_probability (Union[Unset, float]):
            wind_avg (Union[Unset, float]):  Example: 2.
            wind_direction (Union[Unset, float]):  Example: 34.
            wind_direction_cardinal (Union[Unset, str]):  Example: NE.
            wind_gust (Union[Unset, float]):  Example: 3.
            uv (Union[Unset, float]):  Example: 2.
            feels_like (Union[Unset, float]):  Example: 57.
            local_hour (Union[Unset, float]):  Example: 10.
            local_day (Union[Unset, float]):  Example: 23.
     """

    time: Union[Unset, float] = UNSET
    conditions: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    air_temperature: Union[Unset, float] = UNSET
    sea_level_pressure: Union[Unset, float] = UNSET
    relative_humidity: Union[Unset, float] = UNSET
    precip: Union[Unset, float] = UNSET
    precip_probability: Union[Unset, float] = UNSET
    wind_avg: Union[Unset, float] = UNSET
    wind_direction: Union[Unset, float] = UNSET
    wind_direction_cardinal: Union[Unset, str] = UNSET
    wind_gust: Union[Unset, float] = UNSET
    uv: Union[Unset, float] = UNSET
    feels_like: Union[Unset, float] = UNSET
    local_hour: Union[Unset, float] = UNSET
    local_day: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        time = self.time

        conditions = self.conditions

        icon = self.icon

        air_temperature = self.air_temperature

        sea_level_pressure = self.sea_level_pressure

        relative_humidity = self.relative_humidity

        precip = self.precip

        precip_probability = self.precip_probability

        wind_avg = self.wind_avg

        wind_direction = self.wind_direction

        wind_direction_cardinal = self.wind_direction_cardinal

        wind_gust = self.wind_gust

        uv = self.uv

        feels_like = self.feels_like

        local_hour = self.local_hour

        local_day = self.local_day


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if time is not UNSET:
            field_dict["time"] = time
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if icon is not UNSET:
            field_dict["icon"] = icon
        if air_temperature is not UNSET:
            field_dict["air_temperature"] = air_temperature
        if sea_level_pressure is not UNSET:
            field_dict["sea_level_pressure"] = sea_level_pressure
        if relative_humidity is not UNSET:
            field_dict["relative_humidity"] = relative_humidity
        if precip is not UNSET:
            field_dict["precip"] = precip
        if precip_probability is not UNSET:
            field_dict["precip_probability"] = precip_probability
        if wind_avg is not UNSET:
            field_dict["wind_avg"] = wind_avg
        if wind_direction is not UNSET:
            field_dict["wind_direction"] = wind_direction
        if wind_direction_cardinal is not UNSET:
            field_dict["wind_direction_cardinal"] = wind_direction_cardinal
        if wind_gust is not UNSET:
            field_dict["wind_gust"] = wind_gust
        if uv is not UNSET:
            field_dict["uv"] = uv
        if feels_like is not UNSET:
            field_dict["feels_like"] = feels_like
        if local_hour is not UNSET:
            field_dict["local_hour"] = local_hour
        if local_day is not UNSET:
            field_dict["local_day"] = local_day

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        conditions = d.pop("conditions", UNSET)

        icon = d.pop("icon", UNSET)

        air_temperature = d.pop("air_temperature", UNSET)

        sea_level_pressure = d.pop("sea_level_pressure", UNSET)

        relative_humidity = d.pop("relative_humidity", UNSET)

        precip = d.pop("precip", UNSET)

        precip_probability = d.pop("precip_probability", UNSET)

        wind_avg = d.pop("wind_avg", UNSET)

        wind_direction = d.pop("wind_direction", UNSET)

        wind_direction_cardinal = d.pop("wind_direction_cardinal", UNSET)

        wind_gust = d.pop("wind_gust", UNSET)

        uv = d.pop("uv", UNSET)

        feels_like = d.pop("feels_like", UNSET)

        local_hour = d.pop("local_hour", UNSET)

        local_day = d.pop("local_day", UNSET)

        better_forecast_hourly_forecast = cls(
            time=time,
            conditions=conditions,
            icon=icon,
            air_temperature=air_temperature,
            sea_level_pressure=sea_level_pressure,
            relative_humidity=relative_humidity,
            precip=precip,
            precip_probability=precip_probability,
            wind_avg=wind_avg,
            wind_direction=wind_direction,
            wind_direction_cardinal=wind_direction_cardinal,
            wind_gust=wind_gust,
            uv=uv,
            feels_like=feels_like,
            local_hour=local_hour,
            local_day=local_day,
        )


        better_forecast_hourly_forecast.additional_properties = d
        return better_forecast_hourly_forecast

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
