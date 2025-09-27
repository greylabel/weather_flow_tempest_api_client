from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.device_device_type import DeviceDeviceType
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.device_meta import DeviceMeta





T = TypeVar("T", bound="Device")



@_attrs_define
class Device:
    """ 
        Attributes:
            device_id (Union[Unset, int]):  Example: 128.
            serial_number (Union[Unset, str]):  Example: AR-12345678.
            device_meta (Union[Unset, DeviceMeta]):
            device_type (Union[Unset, DeviceDeviceType]):  Example: AR.
            hardware_revision (Union[Unset, str]):  Example: 3.
            firmware_revision (Union[Unset, str]):  Example: 3.
            notes (Union[Unset, str]):
     """

    device_id: Union[Unset, int] = UNSET
    serial_number: Union[Unset, str] = UNSET
    device_meta: Union[Unset, 'DeviceMeta'] = UNSET
    device_type: Union[Unset, DeviceDeviceType] = UNSET
    hardware_revision: Union[Unset, str] = UNSET
    firmware_revision: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.device_meta import DeviceMeta
        device_id = self.device_id

        serial_number = self.serial_number

        device_meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.device_meta, Unset):
            device_meta = self.device_meta.to_dict()

        device_type: Union[Unset, str] = UNSET
        if not isinstance(self.device_type, Unset):
            device_type = self.device_type.value


        hardware_revision = self.hardware_revision

        firmware_revision = self.firmware_revision

        notes = self.notes


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if serial_number is not UNSET:
            field_dict["serial_number"] = serial_number
        if device_meta is not UNSET:
            field_dict["device_meta"] = device_meta
        if device_type is not UNSET:
            field_dict["device_type"] = device_type
        if hardware_revision is not UNSET:
            field_dict["hardware_revision"] = hardware_revision
        if firmware_revision is not UNSET:
            field_dict["firmware_revision"] = firmware_revision
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.device_meta import DeviceMeta
        d = dict(src_dict)
        device_id = d.pop("device_id", UNSET)

        serial_number = d.pop("serial_number", UNSET)

        _device_meta = d.pop("device_meta", UNSET)
        device_meta: Union[Unset, DeviceMeta]
        if isinstance(_device_meta,  Unset):
            device_meta = UNSET
        else:
            device_meta = DeviceMeta.from_dict(_device_meta)




        _device_type = d.pop("device_type", UNSET)
        device_type: Union[Unset, DeviceDeviceType]
        if isinstance(_device_type,  Unset):
            device_type = UNSET
        else:
            device_type = DeviceDeviceType(_device_type)




        hardware_revision = d.pop("hardware_revision", UNSET)

        firmware_revision = d.pop("firmware_revision", UNSET)

        notes = d.pop("notes", UNSET)

        device = cls(
            device_id=device_id,
            serial_number=serial_number,
            device_meta=device_meta,
            device_type=device_type,
            hardware_revision=hardware_revision,
            firmware_revision=firmware_revision,
            notes=notes,
        )


        device.additional_properties = d
        return device

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
