from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.station_meta import StationMeta
  from ..models.station_item import StationItem
  from ..models.device import Device





T = TypeVar("T", bound="Station")



@_attrs_define
class Station:
    """ 
        Attributes:
            station_id (Union[Unset, int]):  Example: 67.
            name (Union[Unset, str]):  Example: Home.
            public_name (Union[Unset, str]):  Example: Public Location Name.
            latitude (Union[Unset, float]):  Example: 29.00724.
            longitude (Union[Unset, float]):  Example: -80.88067.
            station_meta (Union[Unset, StationMeta]):
            devices (Union[Unset, list['Device']]):
            station_items (Union[Unset, list['StationItem']]):
     """

    station_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    public_name: Union[Unset, str] = UNSET
    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    station_meta: Union[Unset, 'StationMeta'] = UNSET
    devices: Union[Unset, list['Device']] = UNSET
    station_items: Union[Unset, list['StationItem']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.station_meta import StationMeta
        from ..models.station_item import StationItem
        from ..models.device import Device
        station_id = self.station_id

        name = self.name

        public_name = self.public_name

        latitude = self.latitude

        longitude = self.longitude

        station_meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.station_meta, Unset):
            station_meta = self.station_meta.to_dict()

        devices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()
                devices.append(devices_item)



        station_items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.station_items, Unset):
            station_items = []
            for station_items_item_data in self.station_items:
                station_items_item = station_items_item_data.to_dict()
                station_items.append(station_items_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if station_id is not UNSET:
            field_dict["station_id"] = station_id
        if name is not UNSET:
            field_dict["name"] = name
        if public_name is not UNSET:
            field_dict["public_name"] = public_name
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if station_meta is not UNSET:
            field_dict["station_meta"] = station_meta
        if devices is not UNSET:
            field_dict["devices"] = devices
        if station_items is not UNSET:
            field_dict["station_items"] = station_items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.station_meta import StationMeta
        from ..models.station_item import StationItem
        from ..models.device import Device
        d = dict(src_dict)
        station_id = d.pop("station_id", UNSET)

        name = d.pop("name", UNSET)

        public_name = d.pop("public_name", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        _station_meta = d.pop("station_meta", UNSET)
        station_meta: Union[Unset, StationMeta]
        if isinstance(_station_meta,  Unset):
            station_meta = UNSET
        else:
            station_meta = StationMeta.from_dict(_station_meta)




        devices = []
        _devices = d.pop("devices", UNSET)
        for devices_item_data in (_devices or []):
            devices_item = Device.from_dict(devices_item_data)



            devices.append(devices_item)


        station_items = []
        _station_items = d.pop("station_items", UNSET)
        for station_items_item_data in (_station_items or []):
            station_items_item = StationItem.from_dict(station_items_item_data)



            station_items.append(station_items_item)


        station = cls(
            station_id=station_id,
            name=name,
            public_name=public_name,
            latitude=latitude,
            longitude=longitude,
            station_meta=station_meta,
            devices=devices,
            station_items=station_items,
        )


        station.additional_properties = d
        return station

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
