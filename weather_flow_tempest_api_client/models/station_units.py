from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="StationUnits")



@_attrs_define
class StationUnits:
    """ 
        Attributes:
            units_temp (Union[Unset, str]):  Example: f.
            units_wind (Union[Unset, str]):  Example: mph.
            units_precip (Union[Unset, str]):  Example: in.
            units_pressure (Union[Unset, str]):  Example: mb.
            units_distance (Union[Unset, str]):  Example: mi.
            units_direction (Union[Unset, str]):  Example: cardinal.
            units_other (Union[Unset, str]):  Example: imperial.
     """

    units_temp: Union[Unset, str] = UNSET
    units_wind: Union[Unset, str] = UNSET
    units_precip: Union[Unset, str] = UNSET
    units_pressure: Union[Unset, str] = UNSET
    units_distance: Union[Unset, str] = UNSET
    units_direction: Union[Unset, str] = UNSET
    units_other: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        units_temp = self.units_temp

        units_wind = self.units_wind

        units_precip = self.units_precip

        units_pressure = self.units_pressure

        units_distance = self.units_distance

        units_direction = self.units_direction

        units_other = self.units_other


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if units_temp is not UNSET:
            field_dict["units_temp"] = units_temp
        if units_wind is not UNSET:
            field_dict["units_wind"] = units_wind
        if units_precip is not UNSET:
            field_dict["units_precip"] = units_precip
        if units_pressure is not UNSET:
            field_dict["units_pressure"] = units_pressure
        if units_distance is not UNSET:
            field_dict["units_distance"] = units_distance
        if units_direction is not UNSET:
            field_dict["units_direction"] = units_direction
        if units_other is not UNSET:
            field_dict["units_other"] = units_other

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        units_temp = d.pop("units_temp", UNSET)

        units_wind = d.pop("units_wind", UNSET)

        units_precip = d.pop("units_precip", UNSET)

        units_pressure = d.pop("units_pressure", UNSET)

        units_distance = d.pop("units_distance", UNSET)

        units_direction = d.pop("units_direction", UNSET)

        units_other = d.pop("units_other", UNSET)

        station_units = cls(
            units_temp=units_temp,
            units_wind=units_wind,
            units_precip=units_precip,
            units_pressure=units_pressure,
            units_distance=units_distance,
            units_direction=units_direction,
            units_other=units_other,
        )


        station_units.additional_properties = d
        return station_units

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
