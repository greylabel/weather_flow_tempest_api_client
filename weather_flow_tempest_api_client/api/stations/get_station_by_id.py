from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.station_set import StationSet
from typing import cast



def _get_kwargs(
    station_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/stations/{station_id}".format(station_id=station_id,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, StationSet]]:
    if response.status_code == 200:
        response_200 = StationSet.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, StationSet]]:
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

) -> Response[Union[Any, StationSet]]:
    """ Find a Station by station_id

     Devices all belong to a Station.  This response contains Station metadata and metadata for the
    Devices in it.  Each user can create multiple Stations.  A Device can only be in one Station at a
    time.  Only devices with a serial_number value can send new observations.  A Device wihout a
    serial_number indicates that Device is no longer active.

    Args:
        station_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StationSet]]
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

) -> Optional[Union[Any, StationSet]]:
    """ Find a Station by station_id

     Devices all belong to a Station.  This response contains Station metadata and metadata for the
    Devices in it.  Each user can create multiple Stations.  A Device can only be in one Station at a
    time.  Only devices with a serial_number value can send new observations.  A Device wihout a
    serial_number indicates that Device is no longer active.

    Args:
        station_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StationSet]
     """


    return sync_detailed(
        station_id=station_id,
client=client,

    ).parsed

async def asyncio_detailed(
    station_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, StationSet]]:
    """ Find a Station by station_id

     Devices all belong to a Station.  This response contains Station metadata and metadata for the
    Devices in it.  Each user can create multiple Stations.  A Device can only be in one Station at a
    time.  Only devices with a serial_number value can send new observations.  A Device wihout a
    serial_number indicates that Device is no longer active.

    Args:
        station_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StationSet]]
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

) -> Optional[Union[Any, StationSet]]:
    """ Find a Station by station_id

     Devices all belong to a Station.  This response contains Station metadata and metadata for the
    Devices in it.  Each user can create multiple Stations.  A Device can only be in one Station at a
    time.  Only devices with a serial_number value can send new observations.  A Device wihout a
    serial_number indicates that Device is no longer active.

    Args:
        station_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StationSet]
     """


    return (await asyncio_detailed(
        station_id=station_id,
client=client,

    )).parsed
