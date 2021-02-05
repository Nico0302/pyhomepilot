from pyhomepilot.utils import reverse_percentage
from .device import Device


class Actuator(Device):
    """Class that represents an Actuator object in the HomePilot API."""

    def __init__(self, *args, **kwargs):
        """Initialize an actuator object."""
        super(Actuator, self).__init__(*args, **kwargs)

    @property
    def position(self) -> str:
        """Return position of the actuator."""
        return self.statusMap["Position"]
    
    async def async_command(self, command: str, value=None):
        """Send a command to the actuator."""
        payload = {
            "name": command,
            "value": value
        }
        await self.auth.request("put", f"devices/{self.did}", json=payload)