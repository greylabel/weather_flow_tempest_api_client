from enum import Enum

class GetBetterForecastUnitsPressure(str, Enum):
    HPA = "hpa"
    INHG = "inhg"
    MB = "mb"
    MMHG = "mmhg"

    def __str__(self) -> str:
        return str(self.value)
