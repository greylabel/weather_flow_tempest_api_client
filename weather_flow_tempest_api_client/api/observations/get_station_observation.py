from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.station_observation import StationObservation
from typing import cast



def _get_kwargs(
    station_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/observations/station/{station_id}".format(station_id=station_id,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, StationObservation]]:
    if response.status_code == 200:
        response_200 = StationObservation.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, StationObservation]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    station_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, StationObservation]]:
    r""" Get the latest Station observation

     Get the latest federated observation for a Station.  This observation is made from the latest Device
    observations that belong to the Station.  If a user has multiple Devices of the same type they are
    able to designate one of them as primary. This is the one used to make the federated
    observation.<br><br>A user can also designate each device as either indoor or outdoor.  All indoor
    observation value fields will end with an \"_indoor\" suffix.  Outdoor observations fields do not
    have a suffix.<br><br>The station_units values represent the units of the Station's owner, not the
    units of the observation values in the API response.

    Args:
        station_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StationObservation]]
     """


    kwargs = _get_kwargs(
        station_id=station_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    station_id: int,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Any, StationObservation]]:
    r""" Get the latest Station observation

     Get the latest federated observation for a Station.  This observation is made from the latest Device
    observations that belong to the Station.  If a user has multiple Devices of the same type they are
    able to designate one of them as primary. This is the one used to make the federated
    observation.<br><br>A user can also designate each device as either indoor or outdoor.  All indoor
    observation value fields will end with an \"_indoor\" suffix.  Outdoor observations fields do not
    have a suffix.<br><br>The station_units values represent the units of the Station's owner, not the
    units of the observation values in the API response.

    Args:
        station_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StationObservation]
     """


    return sync_detailed(
        station_id=station_id,
client=client,

    ).parsed

async def asyncio_detailed(
    station_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, StationObservation]]:
    r""" Get the latest Station observation

     Get the latest federated observation for a Station.  This observation is made from the latest Device
    observations that belong to the Station.  If a user has multiple Devices of the same type they are
    able to designate one of them as primary. This is the one used to make the federated
    observation.<br><br>A user can also designate each device as either indoor or outdoor.  All indoor
    observation value fields will end with an \"_indoor\" suffix.  Outdoor observations fields do not
    have a suffix.<br><br>The station_units values represent the units of the Station's owner, not the
    units of the observation values in the API response.

    Args:
        station_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StationObservation]]
     """


    kwargs = _get_kwargs(
        station_id=station_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    station_id: int,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Any, StationObservation]]:
    r""" Get the latest Station observation

     Get the latest federated observation for a Station.  This observation is made from the latest Device
    observations that belong to the Station.  If a user has multiple Devices of the same type they are
    able to designate one of them as primary. This is the one used to make the federated
    observation.<br><br>A user can also designate each device as either indoor or outdoor.  All indoor
    observation value fields will end with an \"_indoor\" suffix.  Outdoor observations fields do not
    have a suffix.<br><br>The station_units values represent the units of the Station's owner, not the
    units of the observation values in the API response.

    Args:
        station_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StationObservation]
     """


    return (await asyncio_detailed(
        station_id=station_id,
client=client,

    )).parsed
