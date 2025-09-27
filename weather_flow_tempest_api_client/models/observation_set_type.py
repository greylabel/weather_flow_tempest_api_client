from enum import Enum

class ObservationSetType(str, Enum):
    OBS_AIR = "obs_air"
    OBS_SKY = "obs_sky"

    def __str__(self) -> str:
        return str(self.value)
