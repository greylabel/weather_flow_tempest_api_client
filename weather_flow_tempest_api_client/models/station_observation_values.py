from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="StationObservationValues")



@_attrs_define
class StationObservationValues:
    """ 
        Attributes:
            timestamp (Union[Unset, float]):  Example: 1495732068.
            air_temperature (Union[Unset, float]):  Example: 29.1.
            barometric_pressure (Union[Unset, float]):  Example: 1002.9.
            sea_level_pressure (Union[Unset, float]):  Example: 1004.7.
            relative_humidity (Union[Unset, float]):  Example: 77.
            precip (Union[Unset, float]):
            precip_accum_last_1hr (Union[Unset, float]):
            wind_avg (Union[Unset, float]):  Example: 3.5.
            wind_direction (Union[Unset, float]):  Example: 289.
            wind_gust (Union[Unset, float]):  Example: 5.1.
            wind_lull (Union[Unset, float]):  Example: 2.2.
            solar_radiation (Union[Unset, float]):  Example: 330.
            uv (Union[Unset, float]):  Example: 8.
            brightness (Union[Unset, float]):  Example: 7000.
            lightning_strike_last_epoch (Union[Unset, float]):  Example: 1495652340.
            lightning_strike_last_distance (Union[Unset, float]):  Example: 22.
            lightning_strike_count_last_3hr (Union[Unset, float]):
            feels_like (Union[Unset, float]):  Example: 21.4.
            heat_index (Union[Unset, float]):  Example: 21.4.
            wind_chill (Union[Unset, float]):  Example: 21.4.
            dew_point (Union[Unset, float]):  Example: 17.2.
            wet_bulb_temperature (Union[Unset, float]):  Example: 18.6.
            delta_t (Union[Unset, float]):  Example: -2.8.
            air_density (Union[Unset, float]):  Example: 1.18257.
            air_temperature_indoor (Union[Unset, float]):  Example: 29.1.
            barometric_pressure_indoor (Union[Unset, float]):  Example: 1002.9.
            sea_level_pressure_indoor (Union[Unset, float]):  Example: 1004.7.
            relative_humidity_indoor (Union[Unset, float]):  Example: 77.
            precip_indoor (Union[Unset, float]):
            precip_accum_last_1hr_indoor (Union[Unset, float]):
            wind_avg_indoor (Union[Unset, float]):  Example: 3.5.
            wind_direction_indoor (Union[Unset, float]):  Example: 289.
            wind_gust_indoor (Union[Unset, float]):  Example: 5.1.
            wind_lull_indoor (Union[Unset, float]):  Example: 2.2.
            solar_radiation_indoor (Union[Unset, float]):  Example: 330.
            uv_indoor (Union[Unset, float]):  Example: 8.
            brightness_indoor (Union[Unset, float]):  Example: 7000.
            lightning_strike_last_epoch_indoor (Union[Unset, float]):  Example: 1495652340.
            lightning_strike_last_distance_indoor (Union[Unset, float]):  Example: 22.
            lightning_strike_count_last_3hr_indoor (Union[Unset, float]):
            feels_like_indoor (Union[Unset, float]):  Example: 21.4.
            heat_index_indoor (Union[Unset, float]):  Example: 21.4.
            wind_chill_indoor (Union[Unset, float]):  Example: 21.4.
            dew_point_indoor (Union[Unset, float]):  Example: 17.2.
            wet_bulb_temperature_indoor (Union[Unset, float]):  Example: 18.6.
            delta_t_indoor (Union[Unset, float]):  Example: -2.8.
            air_density_indoor (Union[Unset, float]):  Example: 1.18257.
     """

    timestamp: Union[Unset, float] = UNSET
    air_temperature: Union[Unset, float] = UNSET
    barometric_pressure: Union[Unset, float] = UNSET
    sea_level_pressure: Union[Unset, float] = UNSET
    relative_humidity: Union[Unset, float] = UNSET
    precip: Union[Unset, float] = UNSET
    precip_accum_last_1hr: Union[Unset, float] = UNSET
    wind_avg: Union[Unset, float] = UNSET
    wind_direction: Union[Unset, float] = UNSET
    wind_gust: Union[Unset, float] = UNSET
    wind_lull: Union[Unset, float] = UNSET
    solar_radiation: Union[Unset, float] = UNSET
    uv: Union[Unset, float] = UNSET
    brightness: Union[Unset, float] = UNSET
    lightning_strike_last_epoch: Union[Unset, float] = UNSET
    lightning_strike_last_distance: Union[Unset, float] = UNSET
    lightning_strike_count_last_3hr: Union[Unset, float] = UNSET
    feels_like: Union[Unset, float] = UNSET
    heat_index: Union[Unset, float] = UNSET
    wind_chill: Union[Unset, float] = UNSET
    dew_point: Union[Unset, float] = UNSET
    wet_bulb_temperature: Union[Unset, float] = UNSET
    delta_t: Union[Unset, float] = UNSET
    air_density: Union[Unset, float] = UNSET
    air_temperature_indoor: Union[Unset, float] = UNSET
    barometric_pressure_indoor: Union[Unset, float] = UNSET
    sea_level_pressure_indoor: Union[Unset, float] = UNSET
    relative_humidity_indoor: Union[Unset, float] = UNSET
    precip_indoor: Union[Unset, float] = UNSET
    precip_accum_last_1hr_indoor: Union[Unset, float] = UNSET
    wind_avg_indoor: Union[Unset, float] = UNSET
    wind_direction_indoor: Union[Unset, float] = UNSET
    wind_gust_indoor: Union[Unset, float] = UNSET
    wind_lull_indoor: Union[Unset, float] = UNSET
    solar_radiation_indoor: Union[Unset, float] = UNSET
    uv_indoor: Union[Unset, float] = UNSET
    brightness_indoor: Union[Unset, float] = UNSET
    lightning_strike_last_epoch_indoor: Union[Unset, float] = UNSET
    lightning_strike_last_distance_indoor: Union[Unset, float] = UNSET
    lightning_strike_count_last_3hr_indoor: Union[Unset, float] = UNSET
    feels_like_indoor: Union[Unset, float] = UNSET
    heat_index_indoor: Union[Unset, float] = UNSET
    wind_chill_indoor: Union[Unset, float] = UNSET
    dew_point_indoor: Union[Unset, float] = UNSET
    wet_bulb_temperature_indoor: Union[Unset, float] = UNSET
    delta_t_indoor: Union[Unset, float] = UNSET
    air_density_indoor: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        air_temperature = self.air_temperature

        barometric_pressure = self.barometric_pressure

        sea_level_pressure = self.sea_level_pressure

        relative_humidity = self.relative_humidity

        precip = self.precip

        precip_accum_last_1hr = self.precip_accum_last_1hr

        wind_avg = self.wind_avg

        wind_direction = self.wind_direction

        wind_gust = self.wind_gust

        wind_lull = self.wind_lull

        solar_radiation = self.solar_radiation

        uv = self.uv

        brightness = self.brightness

        lightning_strike_last_epoch = self.lightning_strike_last_epoch

        lightning_strike_last_distance = self.lightning_strike_last_distance

        lightning_strike_count_last_3hr = self.lightning_strike_count_last_3hr

        feels_like = self.feels_like

        heat_index = self.heat_index

        wind_chill = self.wind_chill

        dew_point = self.dew_point

        wet_bulb_temperature = self.wet_bulb_temperature

        delta_t = self.delta_t

        air_density = self.air_density

        air_temperature_indoor = self.air_temperature_indoor

        barometric_pressure_indoor = self.barometric_pressure_indoor

        sea_level_pressure_indoor = self.sea_level_pressure_indoor

        relative_humidity_indoor = self.relative_humidity_indoor

        precip_indoor = self.precip_indoor

        precip_accum_last_1hr_indoor = self.precip_accum_last_1hr_indoor

        wind_avg_indoor = self.wind_avg_indoor

        wind_direction_indoor = self.wind_direction_indoor

        wind_gust_indoor = self.wind_gust_indoor

        wind_lull_indoor = self.wind_lull_indoor

        solar_radiation_indoor = self.solar_radiation_indoor

        uv_indoor = self.uv_indoor

        brightness_indoor = self.brightness_indoor

        lightning_strike_last_epoch_indoor = self.lightning_strike_last_epoch_indoor

        lightning_strike_last_distance_indoor = self.lightning_strike_last_distance_indoor

        lightning_strike_count_last_3hr_indoor = self.lightning_strike_count_last_3hr_indoor

        feels_like_indoor = self.feels_like_indoor

        heat_index_indoor = self.heat_index_indoor

        wind_chill_indoor = self.wind_chill_indoor

        dew_point_indoor = self.dew_point_indoor

        wet_bulb_temperature_indoor = self.wet_bulb_temperature_indoor

        delta_t_indoor = self.delta_t_indoor

        air_density_indoor = self.air_density_indoor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if air_temperature is not UNSET:
            field_dict["air_temperature"] = air_temperature
        if barometric_pressure is not UNSET:
            field_dict["barometric_pressure"] = barometric_pressure
        if sea_level_pressure is not UNSET:
            field_dict["sea_level_pressure"] = sea_level_pressure
        if relative_humidity is not UNSET:
            field_dict["relative_humidity"] = relative_humidity
        if precip is not UNSET:
            field_dict["precip"] = precip
        if precip_accum_last_1hr is not UNSET:
            field_dict["precip_accum_last_1hr"] = precip_accum_last_1hr
        if wind_avg is not UNSET:
            field_dict["wind_avg"] = wind_avg
        if wind_direction is not UNSET:
            field_dict["wind_direction"] = wind_direction
        if wind_gust is not UNSET:
            field_dict["wind_gust"] = wind_gust
        if wind_lull is not UNSET:
            field_dict["wind_lull"] = wind_lull
        if solar_radiation is not UNSET:
            field_dict["solar_radiation"] = solar_radiation
        if uv is not UNSET:
            field_dict["uv"] = uv
        if brightness is not UNSET:
            field_dict["brightness"] = brightness
        if lightning_strike_last_epoch is not UNSET:
            field_dict["lightning_strike_last_epoch"] = lightning_strike_last_epoch
        if lightning_strike_last_distance is not UNSET:
            field_dict["lightning_strike_last_distance"] = lightning_strike_last_distance
        if lightning_strike_count_last_3hr is not UNSET:
            field_dict["lightning_strike_count_last_3hr"] = lightning_strike_count_last_3hr
        if feels_like is not UNSET:
            field_dict["feels_like"] = feels_like
        if heat_index is not UNSET:
            field_dict["heat_index"] = heat_index
        if wind_chill is not UNSET:
            field_dict["wind_chill"] = wind_chill
        if dew_point is not UNSET:
            field_dict["dew_point"] = dew_point
        if wet_bulb_temperature is not UNSET:
            field_dict["wet_bulb_temperature"] = wet_bulb_temperature
        if delta_t is not UNSET:
            field_dict["delta_t"] = delta_t
        if air_density is not UNSET:
            field_dict["air_density"] = air_density
        if air_temperature_indoor is not UNSET:
            field_dict["air_temperature_indoor"] = air_temperature_indoor
        if barometric_pressure_indoor is not UNSET:
            field_dict["barometric_pressure_indoor"] = barometric_pressure_indoor
        if sea_level_pressure_indoor is not UNSET:
            field_dict["sea_level_pressure_indoor"] = sea_level_pressure_indoor
        if relative_humidity_indoor is not UNSET:
            field_dict["relative_humidity_indoor"] = relative_humidity_indoor
        if precip_indoor is not UNSET:
            field_dict["precip_indoor"] = precip_indoor
        if precip_accum_last_1hr_indoor is not UNSET:
            field_dict["precip_accum_last_1hr_indoor"] = precip_accum_last_1hr_indoor
        if wind_avg_indoor is not UNSET:
            field_dict["wind_avg_indoor"] = wind_avg_indoor
        if wind_direction_indoor is not UNSET:
            field_dict["wind_direction_indoor"] = wind_direction_indoor
        if wind_gust_indoor is not UNSET:
            field_dict["wind_gust_indoor"] = wind_gust_indoor
        if wind_lull_indoor is not UNSET:
            field_dict["wind_lull_indoor"] = wind_lull_indoor
        if solar_radiation_indoor is not UNSET:
            field_dict["solar_radiation_indoor"] = solar_radiation_indoor
        if uv_indoor is not UNSET:
            field_dict["uv_indoor"] = uv_indoor
        if brightness_indoor is not UNSET:
            field_dict["brightness_indoor"] = brightness_indoor
        if lightning_strike_last_epoch_indoor is not UNSET:
            field_dict["lightning_strike_last_epoch_indoor"] = lightning_strike_last_epoch_indoor
        if lightning_strike_last_distance_indoor is not UNSET:
            field_dict["lightning_strike_last_distance_indoor"] = lightning_strike_last_distance_indoor
        if lightning_strike_count_last_3hr_indoor is not UNSET:
            field_dict["lightning_strike_count_last_3hr_indoor"] = lightning_strike_count_last_3hr_indoor
        if feels_like_indoor is not UNSET:
            field_dict["feels_like_indoor"] = feels_like_indoor
        if heat_index_indoor is not UNSET:
            field_dict["heat_index_indoor"] = heat_index_indoor
        if wind_chill_indoor is not UNSET:
            field_dict["wind_chill_indoor"] = wind_chill_indoor
        if dew_point_indoor is not UNSET:
            field_dict["dew_point_indoor"] = dew_point_indoor
        if wet_bulb_temperature_indoor is not UNSET:
            field_dict["wet_bulb_temperature_indoor"] = wet_bulb_temperature_indoor
        if delta_t_indoor is not UNSET:
            field_dict["delta_t_indoor"] = delta_t_indoor
        if air_density_indoor is not UNSET:
            field_dict["air_density_indoor"] = air_density_indoor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp", UNSET)

        air_temperature = d.pop("air_temperature", UNSET)

        barometric_pressure = d.pop("barometric_pressure", UNSET)

        sea_level_pressure = d.pop("sea_level_pressure", UNSET)

        relative_humidity = d.pop("relative_humidity", UNSET)

        precip = d.pop("precip", UNSET)

        precip_accum_last_1hr = d.pop("precip_accum_last_1hr", UNSET)

        wind_avg = d.pop("wind_avg", UNSET)

        wind_direction = d.pop("wind_direction", UNSET)

        wind_gust = d.pop("wind_gust", UNSET)

        wind_lull = d.pop("wind_lull", UNSET)

        solar_radiation = d.pop("solar_radiation", UNSET)

        uv = d.pop("uv", UNSET)

        brightness = d.pop("brightness", UNSET)

        lightning_strike_last_epoch = d.pop("lightning_strike_last_epoch", UNSET)

        lightning_strike_last_distance = d.pop("lightning_strike_last_distance", UNSET)

        lightning_strike_count_last_3hr = d.pop("lightning_strike_count_last_3hr", UNSET)

        feels_like = d.pop("feels_like", UNSET)

        heat_index = d.pop("heat_index", UNSET)

        wind_chill = d.pop("wind_chill", UNSET)

        dew_point = d.pop("dew_point", UNSET)

        wet_bulb_temperature = d.pop("wet_bulb_temperature", UNSET)

        delta_t = d.pop("delta_t", UNSET)

        air_density = d.pop("air_density", UNSET)

        air_temperature_indoor = d.pop("air_temperature_indoor", UNSET)

        barometric_pressure_indoor = d.pop("barometric_pressure_indoor", UNSET)

        sea_level_pressure_indoor = d.pop("sea_level_pressure_indoor", UNSET)

        relative_humidity_indoor = d.pop("relative_humidity_indoor", UNSET)

        precip_indoor = d.pop("precip_indoor", UNSET)

        precip_accum_last_1hr_indoor = d.pop("precip_accum_last_1hr_indoor", UNSET)

        wind_avg_indoor = d.pop("wind_avg_indoor", UNSET)

        wind_direction_indoor = d.pop("wind_direction_indoor", UNSET)

        wind_gust_indoor = d.pop("wind_gust_indoor", UNSET)

        wind_lull_indoor = d.pop("wind_lull_indoor", UNSET)

        solar_radiation_indoor = d.pop("solar_radiation_indoor", UNSET)

        uv_indoor = d.pop("uv_indoor", UNSET)

        brightness_indoor = d.pop("brightness_indoor", UNSET)

        lightning_strike_last_epoch_indoor = d.pop("lightning_strike_last_epoch_indoor", UNSET)

        lightning_strike_last_distance_indoor = d.pop("lightning_strike_last_distance_indoor", UNSET)

        lightning_strike_count_last_3hr_indoor = d.pop("lightning_strike_count_last_3hr_indoor", UNSET)

        feels_like_indoor = d.pop("feels_like_indoor", UNSET)

        heat_index_indoor = d.pop("heat_index_indoor", UNSET)

        wind_chill_indoor = d.pop("wind_chill_indoor", UNSET)

        dew_point_indoor = d.pop("dew_point_indoor", UNSET)

        wet_bulb_temperature_indoor = d.pop("wet_bulb_temperature_indoor", UNSET)

        delta_t_indoor = d.pop("delta_t_indoor", UNSET)

        air_density_indoor = d.pop("air_density_indoor", UNSET)

        station_observation_values = cls(
            timestamp=timestamp,
            air_temperature=air_temperature,
            barometric_pressure=barometric_pressure,
            sea_level_pressure=sea_level_pressure,
            relative_humidity=relative_humidity,
            precip=precip,
            precip_accum_last_1hr=precip_accum_last_1hr,
            wind_avg=wind_avg,
            wind_direction=wind_direction,
            wind_gust=wind_gust,
            wind_lull=wind_lull,
            solar_radiation=solar_radiation,
            uv=uv,
            brightness=brightness,
            lightning_strike_last_epoch=lightning_strike_last_epoch,
            lightning_strike_last_distance=lightning_strike_last_distance,
            lightning_strike_count_last_3hr=lightning_strike_count_last_3hr,
            feels_like=feels_like,
            heat_index=heat_index,
            wind_chill=wind_chill,
            dew_point=dew_point,
            wet_bulb_temperature=wet_bulb_temperature,
            delta_t=delta_t,
            air_density=air_density,
            air_temperature_indoor=air_temperature_indoor,
            barometric_pressure_indoor=barometric_pressure_indoor,
            sea_level_pressure_indoor=sea_level_pressure_indoor,
            relative_humidity_indoor=relative_humidity_indoor,
            precip_indoor=precip_indoor,
            precip_accum_last_1hr_indoor=precip_accum_last_1hr_indoor,
            wind_avg_indoor=wind_avg_indoor,
            wind_direction_indoor=wind_direction_indoor,
            wind_gust_indoor=wind_gust_indoor,
            wind_lull_indoor=wind_lull_indoor,
            solar_radiation_indoor=solar_radiation_indoor,
            uv_indoor=uv_indoor,
            brightness_indoor=brightness_indoor,
            lightning_strike_last_epoch_indoor=lightning_strike_last_epoch_indoor,
            lightning_strike_last_distance_indoor=lightning_strike_last_distance_indoor,
            lightning_strike_count_last_3hr_indoor=lightning_strike_count_last_3hr_indoor,
            feels_like_indoor=feels_like_indoor,
            heat_index_indoor=heat_index_indoor,
            wind_chill_indoor=wind_chill_indoor,
            dew_point_indoor=dew_point_indoor,
            wet_bulb_temperature_indoor=wet_bulb_temperature_indoor,
            delta_t_indoor=delta_t_indoor,
            air_density_indoor=air_density_indoor,
        )


        station_observation_values.additional_properties = d
        return station_observation_values

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
