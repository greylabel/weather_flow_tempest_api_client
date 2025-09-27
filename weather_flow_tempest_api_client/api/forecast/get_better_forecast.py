from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.better_forecast import BetterForecast
from ...models.get_better_forecast_units_distance import GetBetterForecastUnitsDistance
from ...models.get_better_forecast_units_precip import GetBetterForecastUnitsPrecip
from ...models.get_better_forecast_units_pressure import GetBetterForecastUnitsPressure
from ...models.get_better_forecast_units_temp import GetBetterForecastUnitsTemp
from ...models.get_better_forecast_units_wind import GetBetterForecastUnitsWind
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    station_id: int,
    units_temp: Union[Unset, GetBetterForecastUnitsTemp] = UNSET,
    units_wind: Union[Unset, GetBetterForecastUnitsWind] = UNSET,
    units_pressure: Union[Unset, GetBetterForecastUnitsPressure] = UNSET,
    units_precip: Union[Unset, GetBetterForecastUnitsPrecip] = UNSET,
    units_distance: Union[Unset, GetBetterForecastUnitsDistance] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["station_id"] = station_id

    json_units_temp: Union[Unset, str] = UNSET
    if not isinstance(units_temp, Unset):
        json_units_temp = units_temp.value

    params["units_temp"] = json_units_temp

    json_units_wind: Union[Unset, str] = UNSET
    if not isinstance(units_wind, Unset):
        json_units_wind = units_wind.value

    params["units_wind"] = json_units_wind

    json_units_pressure: Union[Unset, str] = UNSET
    if not isinstance(units_pressure, Unset):
        json_units_pressure = units_pressure.value

    params["units_pressure"] = json_units_pressure

    json_units_precip: Union[Unset, str] = UNSET
    if not isinstance(units_precip, Unset):
        json_units_precip = units_precip.value

    params["units_precip"] = json_units_precip

    json_units_distance: Union[Unset, str] = UNSET
    if not isinstance(units_distance, Unset):
        json_units_distance = units_distance.value

    params["units_distance"] = json_units_distance


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/better_forecast",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, BetterForecast]]:
    if response.status_code == 200:
        response_200 = BetterForecast.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, BetterForecast]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    station_id: int,
    units_temp: Union[Unset, GetBetterForecastUnitsTemp] = UNSET,
    units_wind: Union[Unset, GetBetterForecastUnitsWind] = UNSET,
    units_pressure: Union[Unset, GetBetterForecastUnitsPressure] = UNSET,
    units_precip: Union[Unset, GetBetterForecastUnitsPrecip] = UNSET,
    units_distance: Union[Unset, GetBetterForecastUnitsDistance] = UNSET,

) -> Response[Union[Any, BetterForecast]]:
    """ Get Better Forecast Data

     The better forecast includes current conditions, daily forecast and hourly
    forecast.<br><br><b>Possible Condition Strings:</b><br>Clear<br>Rain Likely<br>Rain
    Possible<br>Snow<br>Snow Possible<br>Wintry Mix Likely<br>Wintry Mix Possible<br>Thunderstorms
    Likely<br>Thunderstorms Possible<br>Windy<br>Foggy<br>Cloudy<br>Partly Cloudy<br>Very Light
    Rain<br><br><b>Possible Icon Values:</b><br>clear-day<br>clear-night<br>cloudy<br>foggy<br>partly-
    cloudy-day<br>partly-cloudy-night<br>possibly-rainy-day<br>possibly-rainy-night<br>possibly-sleet-
    day<br>possibly-sleet-night<br>possibly-snow-day<br>possibly-snow-night<br>possibly-thunderstorm-
    day<br>possibly-thunderstorm-
    night<br>rainy<br>sleet<br>snow<br>thunderstorm<br>windy<br><br><b>Possible Precip Type
    Values:</b><br>rain<br>snow<br>sleet<br>storm<br><br><b>Possible Precip Icon Values:</b><br>chance-
    rain<br>chance-snow<br>chance-sleet<br><br><b>Possible Pressure Trend
    Values:</b><br>falling<br>steady<br>rising<br>unknown<br><br><b>Possible Wind Direction Cardinal Val
    ues:</b><br>N<br>NNE<br>NE<br>ENE<br>E<br>ESE<br>SE<br>SSE<br>S<br>SSW<br>SW<br>WSW<br>W<br>WNW<br>N
    W<br>NNW<br>N

    Args:
        station_id (int):
        units_temp (Union[Unset, GetBetterForecastUnitsTemp]):
        units_wind (Union[Unset, GetBetterForecastUnitsWind]):
        units_pressure (Union[Unset, GetBetterForecastUnitsPressure]):
        units_precip (Union[Unset, GetBetterForecastUnitsPrecip]):
        units_distance (Union[Unset, GetBetterForecastUnitsDistance]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BetterForecast]]
     """


    kwargs = _get_kwargs(
        station_id=station_id,
units_temp=units_temp,
units_wind=units_wind,
units_pressure=units_pressure,
units_precip=units_precip,
units_distance=units_distance,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    station_id: int,
    units_temp: Union[Unset, GetBetterForecastUnitsTemp] = UNSET,
    units_wind: Union[Unset, GetBetterForecastUnitsWind] = UNSET,
    units_pressure: Union[Unset, GetBetterForecastUnitsPressure] = UNSET,
    units_precip: Union[Unset, GetBetterForecastUnitsPrecip] = UNSET,
    units_distance: Union[Unset, GetBetterForecastUnitsDistance] = UNSET,

) -> Optional[Union[Any, BetterForecast]]:
    """ Get Better Forecast Data

     The better forecast includes current conditions, daily forecast and hourly
    forecast.<br><br><b>Possible Condition Strings:</b><br>Clear<br>Rain Likely<br>Rain
    Possible<br>Snow<br>Snow Possible<br>Wintry Mix Likely<br>Wintry Mix Possible<br>Thunderstorms
    Likely<br>Thunderstorms Possible<br>Windy<br>Foggy<br>Cloudy<br>Partly Cloudy<br>Very Light
    Rain<br><br><b>Possible Icon Values:</b><br>clear-day<br>clear-night<br>cloudy<br>foggy<br>partly-
    cloudy-day<br>partly-cloudy-night<br>possibly-rainy-day<br>possibly-rainy-night<br>possibly-sleet-
    day<br>possibly-sleet-night<br>possibly-snow-day<br>possibly-snow-night<br>possibly-thunderstorm-
    day<br>possibly-thunderstorm-
    night<br>rainy<br>sleet<br>snow<br>thunderstorm<br>windy<br><br><b>Possible Precip Type
    Values:</b><br>rain<br>snow<br>sleet<br>storm<br><br><b>Possible Precip Icon Values:</b><br>chance-
    rain<br>chance-snow<br>chance-sleet<br><br><b>Possible Pressure Trend
    Values:</b><br>falling<br>steady<br>rising<br>unknown<br><br><b>Possible Wind Direction Cardinal Val
    ues:</b><br>N<br>NNE<br>NE<br>ENE<br>E<br>ESE<br>SE<br>SSE<br>S<br>SSW<br>SW<br>WSW<br>W<br>WNW<br>N
    W<br>NNW<br>N

    Args:
        station_id (int):
        units_temp (Union[Unset, GetBetterForecastUnitsTemp]):
        units_wind (Union[Unset, GetBetterForecastUnitsWind]):
        units_pressure (Union[Unset, GetBetterForecastUnitsPressure]):
        units_precip (Union[Unset, GetBetterForecastUnitsPrecip]):
        units_distance (Union[Unset, GetBetterForecastUnitsDistance]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BetterForecast]
     """


    return sync_detailed(
        client=client,
station_id=station_id,
units_temp=units_temp,
units_wind=units_wind,
units_pressure=units_pressure,
units_precip=units_precip,
units_distance=units_distance,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    station_id: int,
    units_temp: Union[Unset, GetBetterForecastUnitsTemp] = UNSET,
    units_wind: Union[Unset, GetBetterForecastUnitsWind] = UNSET,
    units_pressure: Union[Unset, GetBetterForecastUnitsPressure] = UNSET,
    units_precip: Union[Unset, GetBetterForecastUnitsPrecip] = UNSET,
    units_distance: Union[Unset, GetBetterForecastUnitsDistance] = UNSET,

) -> Response[Union[Any, BetterForecast]]:
    """ Get Better Forecast Data

     The better forecast includes current conditions, daily forecast and hourly
    forecast.<br><br><b>Possible Condition Strings:</b><br>Clear<br>Rain Likely<br>Rain
    Possible<br>Snow<br>Snow Possible<br>Wintry Mix Likely<br>Wintry Mix Possible<br>Thunderstorms
    Likely<br>Thunderstorms Possible<br>Windy<br>Foggy<br>Cloudy<br>Partly Cloudy<br>Very Light
    Rain<br><br><b>Possible Icon Values:</b><br>clear-day<br>clear-night<br>cloudy<br>foggy<br>partly-
    cloudy-day<br>partly-cloudy-night<br>possibly-rainy-day<br>possibly-rainy-night<br>possibly-sleet-
    day<br>possibly-sleet-night<br>possibly-snow-day<br>possibly-snow-night<br>possibly-thunderstorm-
    day<br>possibly-thunderstorm-
    night<br>rainy<br>sleet<br>snow<br>thunderstorm<br>windy<br><br><b>Possible Precip Type
    Values:</b><br>rain<br>snow<br>sleet<br>storm<br><br><b>Possible Precip Icon Values:</b><br>chance-
    rain<br>chance-snow<br>chance-sleet<br><br><b>Possible Pressure Trend
    Values:</b><br>falling<br>steady<br>rising<br>unknown<br><br><b>Possible Wind Direction Cardinal Val
    ues:</b><br>N<br>NNE<br>NE<br>ENE<br>E<br>ESE<br>SE<br>SSE<br>S<br>SSW<br>SW<br>WSW<br>W<br>WNW<br>N
    W<br>NNW<br>N

    Args:
        station_id (int):
        units_temp (Union[Unset, GetBetterForecastUnitsTemp]):
        units_wind (Union[Unset, GetBetterForecastUnitsWind]):
        units_pressure (Union[Unset, GetBetterForecastUnitsPressure]):
        units_precip (Union[Unset, GetBetterForecastUnitsPrecip]):
        units_distance (Union[Unset, GetBetterForecastUnitsDistance]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BetterForecast]]
     """


    kwargs = _get_kwargs(
        station_id=station_id,
units_temp=units_temp,
units_wind=units_wind,
units_pressure=units_pressure,
units_precip=units_precip,
units_distance=units_distance,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    station_id: int,
    units_temp: Union[Unset, GetBetterForecastUnitsTemp] = UNSET,
    units_wind: Union[Unset, GetBetterForecastUnitsWind] = UNSET,
    units_pressure: Union[Unset, GetBetterForecastUnitsPressure] = UNSET,
    units_precip: Union[Unset, GetBetterForecastUnitsPrecip] = UNSET,
    units_distance: Union[Unset, GetBetterForecastUnitsDistance] = UNSET,

) -> Optional[Union[Any, BetterForecast]]:
    """ Get Better Forecast Data

     The better forecast includes current conditions, daily forecast and hourly
    forecast.<br><br><b>Possible Condition Strings:</b><br>Clear<br>Rain Likely<br>Rain
    Possible<br>Snow<br>Snow Possible<br>Wintry Mix Likely<br>Wintry Mix Possible<br>Thunderstorms
    Likely<br>Thunderstorms Possible<br>Windy<br>Foggy<br>Cloudy<br>Partly Cloudy<br>Very Light
    Rain<br><br><b>Possible Icon Values:</b><br>clear-day<br>clear-night<br>cloudy<br>foggy<br>partly-
    cloudy-day<br>partly-cloudy-night<br>possibly-rainy-day<br>possibly-rainy-night<br>possibly-sleet-
    day<br>possibly-sleet-night<br>possibly-snow-day<br>possibly-snow-night<br>possibly-thunderstorm-
    day<br>possibly-thunderstorm-
    night<br>rainy<br>sleet<br>snow<br>thunderstorm<br>windy<br><br><b>Possible Precip Type
    Values:</b><br>rain<br>snow<br>sleet<br>storm<br><br><b>Possible Precip Icon Values:</b><br>chance-
    rain<br>chance-snow<br>chance-sleet<br><br><b>Possible Pressure Trend
    Values:</b><br>falling<br>steady<br>rising<br>unknown<br><br><b>Possible Wind Direction Cardinal Val
    ues:</b><br>N<br>NNE<br>NE<br>ENE<br>E<br>ESE<br>SE<br>SSE<br>S<br>SSW<br>SW<br>WSW<br>W<br>WNW<br>N
    W<br>NNW<br>N

    Args:
        station_id (int):
        units_temp (Union[Unset, GetBetterForecastUnitsTemp]):
        units_wind (Union[Unset, GetBetterForecastUnitsWind]):
        units_pressure (Union[Unset, GetBetterForecastUnitsPressure]):
        units_precip (Union[Unset, GetBetterForecastUnitsPrecip]):
        units_distance (Union[Unset, GetBetterForecastUnitsDistance]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BetterForecast]
     """


    return (await asyncio_detailed(
        client=client,
station_id=station_id,
units_temp=units_temp,
units_wind=units_wind,
units_pressure=units_pressure,
units_precip=units_precip,
units_distance=units_distance,

    )).parsed
