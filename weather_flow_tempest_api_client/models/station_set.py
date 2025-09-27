from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.station import Station
  from ..models.status import Status





T = TypeVar("T", bound="StationSet")



@_attrs_define
class StationSet:
    """ 
        Attributes:
            status (Union[Unset, Status]):
            locations (Union[Unset, list['Station']]):
     """

    status: Union[Unset, 'Status'] = UNSET
    locations: Union[Unset, list['Station']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.station import Station
        from ..models.status import Status
        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        locations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()
                locations.append(locations_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if status is not UNSET:
            field_dict["status"] = status
        if locations is not UNSET:
            field_dict["locations"] = locations

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.station import Station
        from ..models.status import Status
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: Union[Unset, Status]
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = Status.from_dict(_status)




        locations = []
        _locations = d.pop("locations", UNSET)
        for locations_item_data in (_locations or []):
            locations_item = Station.from_dict(locations_item_data)



            locations.append(locations_item)


        station_set = cls(
            status=status,
            locations=locations,
        )


        station_set.additional_properties = d
        return station_set

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
