from enum import Enum

class GetBetterForecastUnitsPrecip(str, Enum):
    CM = "cm"
    IN = "in"
    MM = "mm"

    def __str__(self) -> str:
        return str(self.value)
