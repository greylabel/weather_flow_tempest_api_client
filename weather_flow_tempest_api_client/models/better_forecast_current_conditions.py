from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="BetterForecastCurrentConditions")



@_attrs_define
class BetterForecastCurrentConditions:
    """ 
        Attributes:
            time (Union[Unset, float]):  Example: 1608668142.
            conditions (Union[Unset, str]):  Example: Clear.
            icon (Union[Unset, str]):  Example: clear-day.
            air_temperature (Union[Unset, float]):  Example: 67.
            sea_level_pressure (Union[Unset, float]):  Example: 30.195.
            station_pressure (Union[Unset, float]):  Example: 30.079.
            pressure_trend (Union[Unset, str]):  Example: falling.
            relative_humidity (Union[Unset, float]):  Example: 55.
            wind_avg (Union[Unset, float]):  Example: 3.2.
            wind_direction (Union[Unset, float]):  Example: 15.
            wind_direction_cardinal (Union[Unset, str]):  Example: NNE.
            wind_direction_icon (Union[Unset, str]):  Example: wind-rose-nne.
            wind_gust (Union[Unset, float]):  Example: 3.4.
            solar_radiation (Union[Unset, float]):  Example: 22.
            uv (Union[Unset, float]):
            brightness (Union[Unset, float]):  Example: 2582.
            feels_like (Union[Unset, float]):  Example: 68.9.
            dew_point (Union[Unset, float]):  Example: 50.
            wet_bulb_temperature (Union[Unset, float]):  Example: 57.
            delta_t (Union[Unset, float]):  Example: 10.
            air_density (Union[Unset, float]):  Example: 0.08.
            lightning_strike_count_last_1hr (Union[Unset, float]):
            lightning_strike_count_last_3hr (Union[Unset, float]):  Example: 1.
            lightning_strike_last_distance (Union[Unset, float]):  Example: 7.
            lightning_strike_last_distance_msg (Union[Unset, str]):  Example: 6 - 8 mi.
            lightning_strike_last_epoch (Union[Unset, float]):  Example: 1608150959.
            precip_accum_local_day (Union[Unset, float]):
            precip_accum_local_yesterday (Union[Unset, float]):
            precip_minutes_local_day (Union[Unset, float]):
            precip_minutes_local_yesterday (Union[Unset, float]):
            is_precip_local_day_rain_check (Union[Unset, bool]):
            is_precip_local_yesterday_rain_check (Union[Unset, float]):  Example: True.
     """

    time: Union[Unset, float] = UNSET
    conditions: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    air_temperature: Union[Unset, float] = UNSET
    sea_level_pressure: Union[Unset, float] = UNSET
    station_pressure: Union[Unset, float] = UNSET
    pressure_trend: Union[Unset, str] = UNSET
    relative_humidity: Union[Unset, float] = UNSET
    wind_avg: Union[Unset, float] = UNSET
    wind_direction: Union[Unset, float] = UNSET
    wind_direction_cardinal: Union[Unset, str] = UNSET
    wind_direction_icon: Union[Unset, str] = UNSET
    wind_gust: Union[Unset, float] = UNSET
    solar_radiation: Union[Unset, float] = UNSET
    uv: Union[Unset, float] = UNSET
    brightness: Union[Unset, float] = UNSET
    feels_like: Union[Unset, float] = UNSET
    dew_point: Union[Unset, float] = UNSET
    wet_bulb_temperature: Union[Unset, float] = UNSET
    delta_t: Union[Unset, float] = UNSET
    air_density: Union[Unset, float] = UNSET
    lightning_strike_count_last_1hr: Union[Unset, float] = UNSET
    lightning_strike_count_last_3hr: Union[Unset, float] = UNSET
    lightning_strike_last_distance: Union[Unset, float] = UNSET
    lightning_strike_last_distance_msg: Union[Unset, str] = UNSET
    lightning_strike_last_epoch: Union[Unset, float] = UNSET
    precip_accum_local_day: Union[Unset, float] = UNSET
    precip_accum_local_yesterday: Union[Unset, float] = UNSET
    precip_minutes_local_day: Union[Unset, float] = UNSET
    precip_minutes_local_yesterday: Union[Unset, float] = UNSET
    is_precip_local_day_rain_check: Union[Unset, bool] = UNSET
    is_precip_local_yesterday_rain_check: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        time = self.time

        conditions = self.conditions

        icon = self.icon

        air_temperature = self.air_temperature

        sea_level_pressure = self.sea_level_pressure

        station_pressure = self.station_pressure

        pressure_trend = self.pressure_trend

        relative_humidity = self.relative_humidity

        wind_avg = self.wind_avg

        wind_direction = self.wind_direction

        wind_direction_cardinal = self.wind_direction_cardinal

        wind_direction_icon = self.wind_direction_icon

        wind_gust = self.wind_gust

        solar_radiation = self.solar_radiation

        uv = self.uv

        brightness = self.brightness

        feels_like = self.feels_like

        dew_point = self.dew_point

        wet_bulb_temperature = self.wet_bulb_temperature

        delta_t = self.delta_t

        air_density = self.air_density

        lightning_strike_count_last_1hr = self.lightning_strike_count_last_1hr

        lightning_strike_count_last_3hr = self.lightning_strike_count_last_3hr

        lightning_strike_last_distance = self.lightning_strike_last_distance

        lightning_strike_last_distance_msg = self.lightning_strike_last_distance_msg

        lightning_strike_last_epoch = self.lightning_strike_last_epoch

        precip_accum_local_day = self.precip_accum_local_day

        precip_accum_local_yesterday = self.precip_accum_local_yesterday

        precip_minutes_local_day = self.precip_minutes_local_day

        precip_minutes_local_yesterday = self.precip_minutes_local_yesterday

        is_precip_local_day_rain_check = self.is_precip_local_day_rain_check

        is_precip_local_yesterday_rain_check = self.is_precip_local_yesterday_rain_check


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
        if station_pressure is not UNSET:
            field_dict["station_pressure"] = station_pressure
        if pressure_trend is not UNSET:
            field_dict["pressure_trend"] = pressure_trend
        if relative_humidity is not UNSET:
            field_dict["relative_humidity"] = relative_humidity
        if wind_avg is not UNSET:
            field_dict["wind_avg"] = wind_avg
        if wind_direction is not UNSET:
            field_dict["wind_direction"] = wind_direction
        if wind_direction_cardinal is not UNSET:
            field_dict["wind_direction_cardinal"] = wind_direction_cardinal
        if wind_direction_icon is not UNSET:
            field_dict["wind_direction_icon"] = wind_direction_icon
        if wind_gust is not UNSET:
            field_dict["wind_gust"] = wind_gust
        if solar_radiation is not UNSET:
            field_dict["solar_radiation"] = solar_radiation
        if uv is not UNSET:
            field_dict["uv"] = uv
        if brightness is not UNSET:
            field_dict["brightness"] = brightness
        if feels_like is not UNSET:
            field_dict["feels_like"] = feels_like
        if dew_point is not UNSET:
            field_dict["dew_point"] = dew_point
        if wet_bulb_temperature is not UNSET:
            field_dict["wet_bulb_temperature"] = wet_bulb_temperature
        if delta_t is not UNSET:
            field_dict["delta_t"] = delta_t
        if air_density is not UNSET:
            field_dict["air_density"] = air_density
        if lightning_strike_count_last_1hr is not UNSET:
            field_dict["lightning_strike_count_last_1hr"] = lightning_strike_count_last_1hr
        if lightning_strike_count_last_3hr is not UNSET:
            field_dict["lightning_strike_count_last_3hr"] = lightning_strike_count_last_3hr
        if lightning_strike_last_distance is not UNSET:
            field_dict["lightning_strike_last_distance"] = lightning_strike_last_distance
        if lightning_strike_last_distance_msg is not UNSET:
            field_dict["lightning_strike_last_distance_msg"] = lightning_strike_last_distance_msg
        if lightning_strike_last_epoch is not UNSET:
            field_dict["lightning_strike_last_epoch"] = lightning_strike_last_epoch
        if precip_accum_local_day is not UNSET:
            field_dict["precip_accum_local_day"] = precip_accum_local_day
        if precip_accum_local_yesterday is not UNSET:
            field_dict["precip_accum_local_yesterday"] = precip_accum_local_yesterday
        if precip_minutes_local_day is not UNSET:
            field_dict["precip_minutes_local_day"] = precip_minutes_local_day
        if precip_minutes_local_yesterday is not UNSET:
            field_dict["precip_minutes_local_yesterday"] = precip_minutes_local_yesterday
        if is_precip_local_day_rain_check is not UNSET:
            field_dict["is_precip_local_day_rain_check"] = is_precip_local_day_rain_check
        if is_precip_local_yesterday_rain_check is not UNSET:
            field_dict["is_precip_local_yesterday_rain_check"] = is_precip_local_yesterday_rain_check

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        conditions = d.pop("conditions", UNSET)

        icon = d.pop("icon", UNSET)

        air_temperature = d.pop("air_temperature", UNSET)

        sea_level_pressure = d.pop("sea_level_pressure", UNSET)

        station_pressure = d.pop("station_pressure", UNSET)

        pressure_trend = d.pop("pressure_trend", UNSET)

        relative_humidity = d.pop("relative_humidity", UNSET)

        wind_avg = d.pop("wind_avg", UNSET)

        wind_direction = d.pop("wind_direction", UNSET)

        wind_direction_cardinal = d.pop("wind_direction_cardinal", UNSET)

        wind_direction_icon = d.pop("wind_direction_icon", UNSET)

        wind_gust = d.pop("wind_gust", UNSET)

        solar_radiation = d.pop("solar_radiation", UNSET)

        uv = d.pop("uv", UNSET)

        brightness = d.pop("brightness", UNSET)

        feels_like = d.pop("feels_like", UNSET)

        dew_point = d.pop("dew_point", UNSET)

        wet_bulb_temperature = d.pop("wet_bulb_temperature", UNSET)

        delta_t = d.pop("delta_t", UNSET)

        air_density = d.pop("air_density", UNSET)

        lightning_strike_count_last_1hr = d.pop("lightning_strike_count_last_1hr", UNSET)

        lightning_strike_count_last_3hr = d.pop("lightning_strike_count_last_3hr", UNSET)

        lightning_strike_last_distance = d.pop("lightning_strike_last_distance", UNSET)

        lightning_strike_last_distance_msg = d.pop("lightning_strike_last_distance_msg", UNSET)

        lightning_strike_last_epoch = d.pop("lightning_strike_last_epoch", UNSET)

        precip_accum_local_day = d.pop("precip_accum_local_day", UNSET)

        precip_accum_local_yesterday = d.pop("precip_accum_local_yesterday", UNSET)

        precip_minutes_local_day = d.pop("precip_minutes_local_day", UNSET)

        precip_minutes_local_yesterday = d.pop("precip_minutes_local_yesterday", UNSET)

        is_precip_local_day_rain_check = d.pop("is_precip_local_day_rain_check", UNSET)

        is_precip_local_yesterday_rain_check = d.pop("is_precip_local_yesterday_rain_check", UNSET)

        better_forecast_current_conditions = cls(
            time=time,
            conditions=conditions,
            icon=icon,
            air_temperature=air_temperature,
            sea_level_pressure=sea_level_pressure,
            station_pressure=station_pressure,
            pressure_trend=pressure_trend,
            relative_humidity=relative_humidity,
            wind_avg=wind_avg,
            wind_direction=wind_direction,
            wind_direction_cardinal=wind_direction_cardinal,
            wind_direction_icon=wind_direction_icon,
            wind_gust=wind_gust,
            solar_radiation=solar_radiation,
            uv=uv,
            brightness=brightness,
            feels_like=feels_like,
            dew_point=dew_point,
            wet_bulb_temperature=wet_bulb_temperature,
            delta_t=delta_t,
            air_density=air_density,
            lightning_strike_count_last_1hr=lightning_strike_count_last_1hr,
            lightning_strike_count_last_3hr=lightning_strike_count_last_3hr,
            lightning_strike_last_distance=lightning_strike_last_distance,
            lightning_strike_last_distance_msg=lightning_strike_last_distance_msg,
            lightning_strike_last_epoch=lightning_strike_last_epoch,
            precip_accum_local_day=precip_accum_local_day,
            precip_accum_local_yesterday=precip_accum_local_yesterday,
            precip_minutes_local_day=precip_minutes_local_day,
            precip_minutes_local_yesterday=precip_minutes_local_yesterday,
            is_precip_local_day_rain_check=is_precip_local_day_rain_check,
            is_precip_local_yesterday_rain_check=is_precip_local_yesterday_rain_check,
        )


        better_forecast_current_conditions.additional_properties = d
        return better_forecast_current_conditions

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
