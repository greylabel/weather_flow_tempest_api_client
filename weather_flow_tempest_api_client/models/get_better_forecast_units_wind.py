from enum import Enum

class GetBetterForecastUnitsWind(str, Enum):
    BFT = "bft"
    KPH = "kph"
    KTS = "kts"
    LFM = "lfm"
    MPH = "mph"
    MPS = "mps"

    def __str__(self) -> str:
        return str(self.value)
