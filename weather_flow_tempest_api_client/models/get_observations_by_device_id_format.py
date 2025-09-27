from enum import Enum

class GetObservationsByDeviceIdFormat(str, Enum):
    CSV = "csv"

    def __str__(self) -> str:
        return str(self.value)
