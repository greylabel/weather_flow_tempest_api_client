from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="StationMeta")



@_attrs_define
class StationMeta:
    """ 
        Attributes:
            elevation (Union[Unset, float]):  Example: 33.2.
            share_with_wf (Union[Unset, bool]):  Default: True. Example: True.
            share_with_wu (Union[Unset, bool]):  Default: True. Example: True.
     """

    elevation: Union[Unset, float] = UNSET
    share_with_wf: Union[Unset, bool] = True
    share_with_wu: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        elevation = self.elevation

        share_with_wf = self.share_with_wf

        share_with_wu = self.share_with_wu


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if elevation is not UNSET:
            field_dict["elevation"] = elevation
        if share_with_wf is not UNSET:
            field_dict["share_with_wf"] = share_with_wf
        if share_with_wu is not UNSET:
            field_dict["share_with_wu"] = share_with_wu

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        elevation = d.pop("elevation", UNSET)

        share_with_wf = d.pop("share_with_wf", UNSET)

        share_with_wu = d.pop("share_with_wu", UNSET)

        station_meta = cls(
            elevation=elevation,
            share_with_wf=share_with_wf,
            share_with_wu=share_with_wu,
        )


        station_meta.additional_properties = d
        return station_meta

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
