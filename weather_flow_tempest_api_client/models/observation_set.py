from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.observation_set_type import ObservationSetType
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.status import Status





T = TypeVar("T", bound="ObservationSet")



@_attrs_define
class ObservationSet:
    """ 
        Attributes:
            status (Union[Unset, Status]):
            device_id (Union[Unset, float]):  Example: 59.
            type_ (Union[Unset, ObservationSetType]):  Example: obs_air.
            obs (Union[Unset, list[list[float]]]):
     """

    status: Union[Unset, 'Status'] = UNSET
    device_id: Union[Unset, float] = UNSET
    type_: Union[Unset, ObservationSetType] = UNSET
    obs: Union[Unset, list[list[float]]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.status import Status
        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        device_id = self.device_id

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        obs: Union[Unset, list[list[float]]] = UNSET
        if not isinstance(self.obs, Unset):
            obs = []
            for obs_item_data in self.obs:
                obs_item = obs_item_data


                obs.append(obs_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if status is not UNSET:
            field_dict["status"] = status
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if obs is not UNSET:
            field_dict["obs"] = obs

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status import Status
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: Union[Unset, Status]
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = Status.from_dict(_status)




        device_id = d.pop("device_id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ObservationSetType]
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = ObservationSetType(_type_)




        obs = []
        _obs = d.pop("obs", UNSET)
        for obs_item_data in (_obs or []):
            obs_item = cast(list[float], obs_item_data)

            obs.append(obs_item)


        observation_set = cls(
            status=status,
            device_id=device_id,
            type_=type_,
            obs=obs,
        )


        observation_set.additional_properties = d
        return observation_set

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
