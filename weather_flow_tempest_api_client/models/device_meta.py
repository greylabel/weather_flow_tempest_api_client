from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.device_meta_environment import DeviceMetaEnvironment
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="DeviceMeta")



@_attrs_define
class DeviceMeta:
    """ 
        Attributes:
            agl (Union[Unset, float]):  Example: 2.2.
            name (Union[Unset, str]):  Example: Pool Air Device.
            environment (Union[Unset, DeviceMetaEnvironment]):  Example: outdoor.
            wifi_network_name (Union[Unset, str]):
     """

    agl: Union[Unset, float] = UNSET
    name: Union[Unset, str] = UNSET
    environment: Union[Unset, DeviceMetaEnvironment] = UNSET
    wifi_network_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        agl = self.agl

        name = self.name

        environment: Union[Unset, str] = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.value


        wifi_network_name = self.wifi_network_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if agl is not UNSET:
            field_dict["agl"] = agl
        if name is not UNSET:
            field_dict["name"] = name
        if environment is not UNSET:
            field_dict["environment"] = environment
        if wifi_network_name is not UNSET:
            field_dict["wifi_network_name"] = wifi_network_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agl = d.pop("agl", UNSET)

        name = d.pop("name", UNSET)

        _environment = d.pop("environment", UNSET)
        environment: Union[Unset, DeviceMetaEnvironment]
        if isinstance(_environment,  Unset):
            environment = UNSET
        else:
            environment = DeviceMetaEnvironment(_environment)




        wifi_network_name = d.pop("wifi_network_name", UNSET)

        device_meta = cls(
            agl=agl,
            name=name,
            environment=environment,
            wifi_network_name=wifi_network_name,
        )


        device_meta.additional_properties = d
        return device_meta

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
