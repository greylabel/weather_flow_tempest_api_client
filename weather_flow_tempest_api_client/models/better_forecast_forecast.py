from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.better_forecast_daily_forecast import BetterForecastDailyForecast
  from ..models.better_forecast_hourly_forecast import BetterForecastHourlyForecast





T = TypeVar("T", bound="BetterForecastForecast")



@_attrs_define
class BetterForecastForecast:
    """ 
        Attributes:
            daily (Union[Unset, list['BetterForecastDailyForecast']]):
            hourly (Union[Unset, list['BetterForecastHourlyForecast']]):
     """

    daily: Union[Unset, list['BetterForecastDailyForecast']] = UNSET
    hourly: Union[Unset, list['BetterForecastHourlyForecast']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.better_forecast_daily_forecast import BetterForecastDailyForecast
        from ..models.better_forecast_hourly_forecast import BetterForecastHourlyForecast
        daily: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.daily, Unset):
            daily = []
            for daily_item_data in self.daily:
                daily_item = daily_item_data.to_dict()
                daily.append(daily_item)



        hourly: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.hourly, Unset):
            hourly = []
            for hourly_item_data in self.hourly:
                hourly_item = hourly_item_data.to_dict()
                hourly.append(hourly_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if daily is not UNSET:
            field_dict["daily"] = daily
        if hourly is not UNSET:
            field_dict["hourly"] = hourly

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.better_forecast_daily_forecast import BetterForecastDailyForecast
        from ..models.better_forecast_hourly_forecast import BetterForecastHourlyForecast
        d = dict(src_dict)
        daily = []
        _daily = d.pop("daily", UNSET)
        for daily_item_data in (_daily or []):
            daily_item = BetterForecastDailyForecast.from_dict(daily_item_data)



            daily.append(daily_item)


        hourly = []
        _hourly = d.pop("hourly", UNSET)
        for hourly_item_data in (_hourly or []):
            hourly_item = BetterForecastHourlyForecast.from_dict(hourly_item_data)



            hourly.append(hourly_item)


        better_forecast_forecast = cls(
            daily=daily,
            hourly=hourly,
        )


        better_forecast_forecast.additional_properties = d
        return better_forecast_forecast

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
