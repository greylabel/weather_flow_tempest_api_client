from enum import Enum

class DeviceDeviceType(str, Enum):
    AR = "AR"
    SK = "SK"

    def __str__(self) -> str:
        return str(self.value)
