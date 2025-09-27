from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.better_forecast_forecast import BetterForecastForecast
  from ..models.better_forecast_units import BetterForecastUnits
  from ..models.status import Status
  from ..models.better_forecast_current_conditions import BetterForecastCurrentConditions





T = TypeVar("T", bound="BetterForecast")



@_attrs_define
class BetterForecast:
    """ 
        Attributes:
            status (Union[Unset, Status]):
            current_conditions (Union[Unset, BetterForecastCurrentConditions]):
            forecast (Union[Unset, BetterForecastForecast]):
            units (Union[Unset, BetterForecastUnits]):
            latitude (Union[Unset, float]):  Example: 29.00724.
            longitude (Union[Unset, float]):  Example: -80.88067.
            timezone (Union[Unset, str]):  Example: America/New_York.
            timezone_offset_minutes (Union[Unset, float]):  Example: -300.
     """

    status: Union[Unset, 'Status'] = UNSET
    current_conditions: Union[Unset, 'BetterForecastCurrentConditions'] = UNSET
    forecast: Union[Unset, 'BetterForecastForecast'] = UNSET
    units: Union[Unset, 'BetterForecastUnits'] = UNSET
    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    timezone: Union[Unset, str] = UNSET
    timezone_offset_minutes: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.better_forecast_forecast import BetterForecastForecast
        from ..models.better_forecast_units import BetterForecastUnits
        from ..models.status import Status
        from ..models.better_forecast_current_conditions import BetterForecastCurrentConditions
        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        current_conditions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.current_conditions, Unset):
            current_conditions = self.current_conditions.to_dict()

        forecast: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.forecast, Unset):
            forecast = self.forecast.to_dict()

        units: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.units, Unset):
            units = self.units.to_dict()

        latitude = self.latitude

        longitude = self.longitude

        timezone = self.timezone

        timezone_offset_minutes = self.timezone_offset_minutes


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if status is not UNSET:
            field_dict["status"] = status
        if current_conditions is not UNSET:
            field_dict["current_conditions"] = current_conditions
        if forecast is not UNSET:
            field_dict["forecast"] = forecast
        if units is not UNSET:
            field_dict["units"] = units
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if timezone_offset_minutes is not UNSET:
            field_dict["timezone_offset_minutes"] = timezone_offset_minutes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.better_forecast_forecast import BetterForecastForecast
        from ..models.better_forecast_units import BetterForecastUnits
        from ..models.status import Status
        from ..models.better_forecast_current_conditions import BetterForecastCurrentConditions
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: Union[Unset, Status]
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = Status.from_dict(_status)




        _current_conditions = d.pop("current_conditions", UNSET)
        current_conditions: Union[Unset, BetterForecastCurrentConditions]
        if isinstance(_current_conditions,  Unset):
            current_conditions = UNSET
        else:
            current_conditions = BetterForecastCurrentConditions.from_dict(_current_conditions)




        _forecast = d.pop("forecast", UNSET)
        forecast: Union[Unset, BetterForecastForecast]
        if isinstance(_forecast,  Unset):
            forecast = UNSET
        else:
            forecast = BetterForecastForecast.from_dict(_forecast)




        _units = d.pop("units", UNSET)
        units: Union[Unset, BetterForecastUnits]
        if isinstance(_units,  Unset):
            units = UNSET
        else:
            units = BetterForecastUnits.from_dict(_units)




        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        timezone = d.pop("timezone", UNSET)

        timezone_offset_minutes = d.pop("timezone_offset_minutes", UNSET)

        better_forecast = cls(
            status=status,
            current_conditions=current_conditions,
            forecast=forecast,
            units=units,
            latitude=latitude,
            longitude=longitude,
            timezone=timezone,
            timezone_offset_minutes=timezone_offset_minutes,
        )


        better_forecast.additional_properties = d
        return better_forecast

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
