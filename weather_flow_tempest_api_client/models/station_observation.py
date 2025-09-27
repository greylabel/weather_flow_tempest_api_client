from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.status import Status
  from ..models.station_units import StationUnits
  from ..models.station_observation_values import StationObservationValues





T = TypeVar("T", bound="StationObservation")



@_attrs_define
class StationObservation:
    """ 
        Attributes:
            status (Union[Unset, Status]):
            station_units (Union[Unset, StationUnits]):
            station_id (Union[Unset, int]):  Example: 67.
            station_name (Union[Unset, str]):  Example: Home.
            public_name (Union[Unset, str]):  Example: Public Location Name.
            latitude (Union[Unset, float]):  Example: 29.00724.
            longitude (Union[Unset, float]):  Example: -80.88067.
            timezone (Union[Unset, str]):  Example: America/New_York.
            elevation (Union[Unset, float]):  Example: 21.845.
            obs (Union[Unset, list['StationObservationValues']]):
     """

    status: Union[Unset, 'Status'] = UNSET
    station_units: Union[Unset, 'StationUnits'] = UNSET
    station_id: Union[Unset, int] = UNSET
    station_name: Union[Unset, str] = UNSET
    public_name: Union[Unset, str] = UNSET
    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    timezone: Union[Unset, str] = UNSET
    elevation: Union[Unset, float] = UNSET
    obs: Union[Unset, list['StationObservationValues']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.status import Status
        from ..models.station_units import StationUnits
        from ..models.station_observation_values import StationObservationValues
        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        station_units: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.station_units, Unset):
            station_units = self.station_units.to_dict()

        station_id = self.station_id

        station_name = self.station_name

        public_name = self.public_name

        latitude = self.latitude

        longitude = self.longitude

        timezone = self.timezone

        elevation = self.elevation

        obs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.obs, Unset):
            obs = []
            for obs_item_data in self.obs:
                obs_item = obs_item_data.to_dict()
                obs.append(obs_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if status is not UNSET:
            field_dict["status"] = status
        if station_units is not UNSET:
            field_dict["station_units"] = station_units
        if station_id is not UNSET:
            field_dict["station_id"] = station_id
        if station_name is not UNSET:
            field_dict["station_name"] = station_name
        if public_name is not UNSET:
            field_dict["public_name"] = public_name
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if elevation is not UNSET:
            field_dict["elevation"] = elevation
        if obs is not UNSET:
            field_dict["obs"] = obs

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status import Status
        from ..models.station_units import StationUnits
        from ..models.station_observation_values import StationObservationValues
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: Union[Unset, Status]
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = Status.from_dict(_status)




        _station_units = d.pop("station_units", UNSET)
        station_units: Union[Unset, StationUnits]
        if isinstance(_station_units,  Unset):
            station_units = UNSET
        else:
            station_units = StationUnits.from_dict(_station_units)




        station_id = d.pop("station_id", UNSET)

        station_name = d.pop("station_name", UNSET)

        public_name = d.pop("public_name", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        timezone = d.pop("timezone", UNSET)

        elevation = d.pop("elevation", UNSET)

        obs = []
        _obs = d.pop("obs", UNSET)
        for obs_item_data in (_obs or []):
            obs_item = StationObservationValues.from_dict(obs_item_data)



            obs.append(obs_item)


        station_observation = cls(
            status=status,
            station_units=station_units,
            station_id=station_id,
            station_name=station_name,
            public_name=public_name,
            latitude=latitude,
            longitude=longitude,
            timezone=timezone,
            elevation=elevation,
            obs=obs,
        )


        station_observation.additional_properties = d
        return station_observation

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
