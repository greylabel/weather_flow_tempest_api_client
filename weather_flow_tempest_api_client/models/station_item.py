from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="StationItem")



@_attrs_define
class StationItem:
    """ 
        Attributes:
            location_item_id (Union[Unset, int]):  Example: 55.
            station_id (Union[Unset, int]):  Example: 67.
            device_id (Union[Unset, int]):  Example: 55.
            item (Union[Unset, str]):  Example: air_temperature_humidity.
     """

    location_item_id: Union[Unset, int] = UNSET
    station_id: Union[Unset, int] = UNSET
    device_id: Union[Unset, int] = UNSET
    item: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        location_item_id = self.location_item_id

        station_id = self.station_id

        device_id = self.device_id

        item = self.item


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if location_item_id is not UNSET:
            field_dict["location_item_id"] = location_item_id
        if station_id is not UNSET:
            field_dict["station_id"] = station_id
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if item is not UNSET:
            field_dict["item"] = item

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        location_item_id = d.pop("location_item_id", UNSET)

        station_id = d.pop("station_id", UNSET)

        device_id = d.pop("device_id", UNSET)

        item = d.pop("item", UNSET)

        station_item = cls(
            location_item_id=location_item_id,
            station_id=station_id,
            device_id=device_id,
            item=item,
        )


        station_item.additional_properties = d
        return station_item

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
