from enum import Enum

class GetBetterForecastUnitsDistance(str, Enum):
    KM = "km"
    MI = "mi"

    def __str__(self) -> str:
        return str(self.value)
