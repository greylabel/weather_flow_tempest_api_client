from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_observations_by_device_id_format import GetObservationsByDeviceIdFormat
from ...models.observation_set import ObservationSet
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    device_id: int,
    *,
    day_offset: Union[Unset, int] = UNSET,
    time_start: Union[Unset, int] = UNSET,
    time_end: Union[Unset, int] = UNSET,
    format_: Union[Unset, GetObservationsByDeviceIdFormat] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["day_offset"] = day_offset

    params["time_start"] = time_start

    params["time_end"] = time_end

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/observations/device/{device_id}".format(device_id=device_id,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ObservationSet]]:
    if response.status_code == 200:
        response_200 = ObservationSet.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ObservationSet]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    device_id: int,
    *,
    client: AuthenticatedClient,
    day_offset: Union[Unset, int] = UNSET,
    time_start: Union[Unset, int] = UNSET,
    time_end: Union[Unset, int] = UNSET,
    format_: Union[Unset, GetObservationsByDeviceIdFormat] = UNSET,

) -> Response[Union[Any, ObservationSet]]:
    r""" Get Observations for a Single Device

     Get observations for a Device(Air,Sky,Tempest) by using the device_id as the key.  You can find
    device_id values in the response from the Stations service  You can get observations using several
    filters (latest, time range, day offset).

    Use the \"type\" value to determine the layout of the observations values.  The \"obs\" object is an
    array of observations.  Each observation is an array of observation values (see layout
    below).<br><br>**Air**  (type=\"obs_air\")<br>Observation Layout<br>0 - Epoch (seconds UTC)<br>1 -
    Station Pressure (MB)<br>2 - Air Temperature (C)<br>3 - Relative Humidity (%)<br>4 - Lightning
    Strike Count<br>5 - Lightning Strike Average Distance (km)<br>6 - Battery (volts)<br>7 - Report
    Interval (minutes)<br><br>**Sky** (type=\"obs_sky\")<br>Observation Layout<br>0 - Epoch (seconds
    UTC)<br>1 - Illuminance (lux)<br>2 - UV (index)<br>3 - Rain Accumulation (mm)<br>4 - Wind Lull
    (m/s)<br>5 - Wind Avg (m/s)<br>6 - Wind Gust (m/s)<br>7 - Wind Direction (degrees)<br>8 - Battery
    (volts)<br>9 - Report Interval (minutes)<br>10 - Solar Radiation (W/m^2)<br>11 - Local Day Rain
    Accumulation (mm)<br>12 - Precipitation Type (0 = none, 1 = rain, 2 = hail, 3 = rain + hail
    (experimental))<br>13 - Wind Sample Interval (seconds)<br>14 - <a
    href='https://help.weatherflow.com/hc/en-us/articles/360024436634' target='_blank'>NC Rain</a>
    (mm)<br>15 - Local Day <a href='https://help.weatherflow.com/hc/en-us/articles/360024436634'
    target='_blank'>NC Rain</a> Accumulation (mm)<br>16 - Precipitation Analysis Type (0 = none, 1 =
    Rain Check with user display on, 2 = Rain Check with user display off)<br><br>**Tempest**
    (type=\"obs_st\")<br>Observation Layout<br>0 - Epoch (Seconds UTC)<br>1 - Wind Lull  (m/s)<br>2 -
    Wind Avg (m/s)<br>3 - Wind Gust (m/s)<br>4 - Wind Direction (degrees)<br>5 - Wind Sample Interval
    (seconds)<br>6 - Pressure (MB)<br>7 - Air Temperature (C)<br>8 - Relative Humidity (%)<br>9 -
    Illuminance (lux)<br>10 - UV (index)<br>11 - Solar Radiation (W/m^2)<br>12 - Rain Accumulation
    (mm)<br>13 - Precipitation Type (0 = none, 1 = rain, 2 = hail,  3 = rain + hail
    (experimental))<br>14 - Average Strike Distance (km)<br>15 - Strike Count<br>16 - Battery
    (volts)<br>17 - Report Interval (minutes)<br>18 - Local Day Rain Accumulation (mm)<br>19 - <a
    href='https://help.weatherflow.com/hc/en-us/articles/360024436634' target='_blank'>NC Rain</a>
    Accumulation (mm)<br>20 - Local Day <a href='https://help.weatherflow.com/hc/en-
    us/articles/360024436634' target='_blank'>NC Rain</a> Accumulation (mm)<br>21 - Precipitation
    Aanalysis Type (0 = none, 1 = Rain Check with user display on, 2 = Rain Check with user display off)

    Args:
        device_id (int):
        day_offset (Union[Unset, int]):
        time_start (Union[Unset, int]):
        time_end (Union[Unset, int]):
        format_ (Union[Unset, GetObservationsByDeviceIdFormat]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ObservationSet]]
     """


    kwargs = _get_kwargs(
        device_id=device_id,
day_offset=day_offset,
time_start=time_start,
time_end=time_end,
format_=format_,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    device_id: int,
    *,
    client: AuthenticatedClient,
    day_offset: Union[Unset, int] = UNSET,
    time_start: Union[Unset, int] = UNSET,
    time_end: Union[Unset, int] = UNSET,
    format_: Union[Unset, GetObservationsByDeviceIdFormat] = UNSET,

) -> Optional[Union[Any, ObservationSet]]:
    r""" Get Observations for a Single Device

     Get observations for a Device(Air,Sky,Tempest) by using the device_id as the key.  You can find
    device_id values in the response from the Stations service  You can get observations using several
    filters (latest, time range, day offset).

    Use the \"type\" value to determine the layout of the observations values.  The \"obs\" object is an
    array of observations.  Each observation is an array of observation values (see layout
    below).<br><br>**Air**  (type=\"obs_air\")<br>Observation Layout<br>0 - Epoch (seconds UTC)<br>1 -
    Station Pressure (MB)<br>2 - Air Temperature (C)<br>3 - Relative Humidity (%)<br>4 - Lightning
    Strike Count<br>5 - Lightning Strike Average Distance (km)<br>6 - Battery (volts)<br>7 - Report
    Interval (minutes)<br><br>**Sky** (type=\"obs_sky\")<br>Observation Layout<br>0 - Epoch (seconds
    UTC)<br>1 - Illuminance (lux)<br>2 - UV (index)<br>3 - Rain Accumulation (mm)<br>4 - Wind Lull
    (m/s)<br>5 - Wind Avg (m/s)<br>6 - Wind Gust (m/s)<br>7 - Wind Direction (degrees)<br>8 - Battery
    (volts)<br>9 - Report Interval (minutes)<br>10 - Solar Radiation (W/m^2)<br>11 - Local Day Rain
    Accumulation (mm)<br>12 - Precipitation Type (0 = none, 1 = rain, 2 = hail, 3 = rain + hail
    (experimental))<br>13 - Wind Sample Interval (seconds)<br>14 - <a
    href='https://help.weatherflow.com/hc/en-us/articles/360024436634' target='_blank'>NC Rain</a>
    (mm)<br>15 - Local Day <a href='https://help.weatherflow.com/hc/en-us/articles/360024436634'
    target='_blank'>NC Rain</a> Accumulation (mm)<br>16 - Precipitation Analysis Type (0 = none, 1 =
    Rain Check with user display on, 2 = Rain Check with user display off)<br><br>**Tempest**
    (type=\"obs_st\")<br>Observation Layout<br>0 - Epoch (Seconds UTC)<br>1 - Wind Lull  (m/s)<br>2 -
    Wind Avg (m/s)<br>3 - Wind Gust (m/s)<br>4 - Wind Direction (degrees)<br>5 - Wind Sample Interval
    (seconds)<br>6 - Pressure (MB)<br>7 - Air Temperature (C)<br>8 - Relative Humidity (%)<br>9 -
    Illuminance (lux)<br>10 - UV (index)<br>11 - Solar Radiation (W/m^2)<br>12 - Rain Accumulation
    (mm)<br>13 - Precipitation Type (0 = none, 1 = rain, 2 = hail,  3 = rain + hail
    (experimental))<br>14 - Average Strike Distance (km)<br>15 - Strike Count<br>16 - Battery
    (volts)<br>17 - Report Interval (minutes)<br>18 - Local Day Rain Accumulation (mm)<br>19 - <a
    href='https://help.weatherflow.com/hc/en-us/articles/360024436634' target='_blank'>NC Rain</a>
    Accumulation (mm)<br>20 - Local Day <a href='https://help.weatherflow.com/hc/en-
    us/articles/360024436634' target='_blank'>NC Rain</a> Accumulation (mm)<br>21 - Precipitation
    Aanalysis Type (0 = none, 1 = Rain Check with user display on, 2 = Rain Check with user display off)

    Args:
        device_id (int):
        day_offset (Union[Unset, int]):
        time_start (Union[Unset, int]):
        time_end (Union[Unset, int]):
        format_ (Union[Unset, GetObservationsByDeviceIdFormat]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ObservationSet]
     """


    return sync_detailed(
        device_id=device_id,
client=client,
day_offset=day_offset,
time_start=time_start,
time_end=time_end,
format_=format_,

    ).parsed

async def asyncio_detailed(
    device_id: int,
    *,
    client: AuthenticatedClient,
    day_offset: Union[Unset, int] = UNSET,
    time_start: Union[Unset, int] = UNSET,
    time_end: Union[Unset, int] = UNSET,
    format_: Union[Unset, GetObservationsByDeviceIdFormat] = UNSET,

) -> Response[Union[Any, ObservationSet]]:
    r""" Get Observations for a Single Device

     Get observations for a Device(Air,Sky,Tempest) by using the device_id as the key.  You can find
    device_id values in the response from the Stations service  You can get observations using several
    filters (latest, time range, day offset).

    Use the \"type\" value to determine the layout of the observations values.  The \"obs\" object is an
    array of observations.  Each observation is an array of observation values (see layout
    below).<br><br>**Air**  (type=\"obs_air\")<br>Observation Layout<br>0 - Epoch (seconds UTC)<br>1 -
    Station Pressure (MB)<br>2 - Air Temperature (C)<br>3 - Relative Humidity (%)<br>4 - Lightning
    Strike Count<br>5 - Lightning Strike Average Distance (km)<br>6 - Battery (volts)<br>7 - Report
    Interval (minutes)<br><br>**Sky** (type=\"obs_sky\")<br>Observation Layout<br>0 - Epoch (seconds
    UTC)<br>1 - Illuminance (lux)<br>2 - UV (index)<br>3 - Rain Accumulation (mm)<br>4 - Wind Lull
    (m/s)<br>5 - Wind Avg (m/s)<br>6 - Wind Gust (m/s)<br>7 - Wind Direction (degrees)<br>8 - Battery
    (volts)<br>9 - Report Interval (minutes)<br>10 - Solar Radiation (W/m^2)<br>11 - Local Day Rain
    Accumulation (mm)<br>12 - Precipitation Type (0 = none, 1 = rain, 2 = hail, 3 = rain + hail
    (experimental))<br>13 - Wind Sample Interval (seconds)<br>14 - <a
    href='https://help.weatherflow.com/hc/en-us/articles/360024436634' target='_blank'>NC Rain</a>
    (mm)<br>15 - Local Day <a href='https://help.weatherflow.com/hc/en-us/articles/360024436634'
    target='_blank'>NC Rain</a> Accumulation (mm)<br>16 - Precipitation Analysis Type (0 = none, 1 =
    Rain Check with user display on, 2 = Rain Check with user display off)<br><br>**Tempest**
    (type=\"obs_st\")<br>Observation Layout<br>0 - Epoch (Seconds UTC)<br>1 - Wind Lull  (m/s)<br>2 -
    Wind Avg (m/s)<br>3 - Wind Gust (m/s)<br>4 - Wind Direction (degrees)<br>5 - Wind Sample Interval
    (seconds)<br>6 - Pressure (MB)<br>7 - Air Temperature (C)<br>8 - Relative Humidity (%)<br>9 -
    Illuminance (lux)<br>10 - UV (index)<br>11 - Solar Radiation (W/m^2)<br>12 - Rain Accumulation
    (mm)<br>13 - Precipitation Type (0 = none, 1 = rain, 2 = hail,  3 = rain + hail
    (experimental))<br>14 - Average Strike Distance (km)<br>15 - Strike Count<br>16 - Battery
    (volts)<br>17 - Report Interval (minutes)<br>18 - Local Day Rain Accumulation (mm)<br>19 - <a
    href='https://help.weatherflow.com/hc/en-us/articles/360024436634' target='_blank'>NC Rain</a>
    Accumulation (mm)<br>20 - Local Day <a href='https://help.weatherflow.com/hc/en-
    us/articles/360024436634' target='_blank'>NC Rain</a> Accumulation (mm)<br>21 - Precipitation
    Aanalysis Type (0 = none, 1 = Rain Check with user display on, 2 = Rain Check with user display off)

    Args:
        device_id (int):
        day_offset (Union[Unset, int]):
        time_start (Union[Unset, int]):
        time_end (Union[Unset, int]):
        format_ (Union[Unset, GetObservationsByDeviceIdFormat]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ObservationSet]]
     """


    kwargs = _get_kwargs(
        device_id=device_id,
day_offset=day_offset,
time_start=time_start,
time_end=time_end,
format_=format_,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    device_id: int,
    *,
    client: AuthenticatedClient,
    day_offset: Union[Unset, int] = UNSET,
    time_start: Union[Unset, int] = UNSET,
    time_end: Union[Unset, int] = UNSET,
    format_: Union[Unset, GetObservationsByDeviceIdFormat] = UNSET,

) -> Optional[Union[Any, ObservationSet]]:
    r""" Get Observations for a Single Device

     Get observations for a Device(Air,Sky,Tempest) by using the device_id as the key.  You can find
    device_id values in the response from the Stations service  You can get observations using several
    filters (latest, time range, day offset).

    Use the \"type\" value to determine the layout of the observations values.  The \"obs\" object is an
    array of observations.  Each observation is an array of observation values (see layout
    below).<br><br>**Air**  (type=\"obs_air\")<br>Observation Layout<br>0 - Epoch (seconds UTC)<br>1 -
    Station Pressure (MB)<br>2 - Air Temperature (C)<br>3 - Relative Humidity (%)<br>4 - Lightning
    Strike Count<br>5 - Lightning Strike Average Distance (km)<br>6 - Battery (volts)<br>7 - Report
    Interval (minutes)<br><br>**Sky** (type=\"obs_sky\")<br>Observation Layout<br>0 - Epoch (seconds
    UTC)<br>1 - Illuminance (lux)<br>2 - UV (index)<br>3 - Rain Accumulation (mm)<br>4 - Wind Lull
    (m/s)<br>5 - Wind Avg (m/s)<br>6 - Wind Gust (m/s)<br>7 - Wind Direction (degrees)<br>8 - Battery
    (volts)<br>9 - Report Interval (minutes)<br>10 - Solar Radiation (W/m^2)<br>11 - Local Day Rain
    Accumulation (mm)<br>12 - Precipitation Type (0 = none, 1 = rain, 2 = hail, 3 = rain + hail
    (experimental))<br>13 - Wind Sample Interval (seconds)<br>14 - <a
    href='https://help.weatherflow.com/hc/en-us/articles/360024436634' target='_blank'>NC Rain</a>
    (mm)<br>15 - Local Day <a href='https://help.weatherflow.com/hc/en-us/articles/360024436634'
    target='_blank'>NC Rain</a> Accumulation (mm)<br>16 - Precipitation Analysis Type (0 = none, 1 =
    Rain Check with user display on, 2 = Rain Check with user display off)<br><br>**Tempest**
    (type=\"obs_st\")<br>Observation Layout<br>0 - Epoch (Seconds UTC)<br>1 - Wind Lull  (m/s)<br>2 -
    Wind Avg (m/s)<br>3 - Wind Gust (m/s)<br>4 - Wind Direction (degrees)<br>5 - Wind Sample Interval
    (seconds)<br>6 - Pressure (MB)<br>7 - Air Temperature (C)<br>8 - Relative Humidity (%)<br>9 -
    Illuminance (lux)<br>10 - UV (index)<br>11 - Solar Radiation (W/m^2)<br>12 - Rain Accumulation
    (mm)<br>13 - Precipitation Type (0 = none, 1 = rain, 2 = hail,  3 = rain + hail
    (experimental))<br>14 - Average Strike Distance (km)<br>15 - Strike Count<br>16 - Battery
    (volts)<br>17 - Report Interval (minutes)<br>18 - Local Day Rain Accumulation (mm)<br>19 - <a
    href='https://help.weatherflow.com/hc/en-us/articles/360024436634' target='_blank'>NC Rain</a>
    Accumulation (mm)<br>20 - Local Day <a href='https://help.weatherflow.com/hc/en-
    us/articles/360024436634' target='_blank'>NC Rain</a> Accumulation (mm)<br>21 - Precipitation
    Aanalysis Type (0 = none, 1 = Rain Check with user display on, 2 = Rain Check with user display off)

    Args:
        device_id (int):
        day_offset (Union[Unset, int]):
        time_start (Union[Unset, int]):
        time_end (Union[Unset, int]):
        format_ (Union[Unset, GetObservationsByDeviceIdFormat]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ObservationSet]
     """


    return (await asyncio_detailed(
        device_id=device_id,
client=client,
day_offset=day_offset,
time_start=time_start,
time_end=time_end,
format_=format_,

    )).parsed
