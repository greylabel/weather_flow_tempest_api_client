from enum import Enum

class DeviceMetaEnvironment(str, Enum):
    INDOOR = "indoor"
    OUTDOOR = "outdoor"

    def __str__(self) -> str:
        return str(self.value)
