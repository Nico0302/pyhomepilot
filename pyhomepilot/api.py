from typing import List

from pyhomepilot.auth import Auth
from pyhomepilot.devices import (
    Actuator, 
    Blind, 
    Device
)


ACTUATOR_CLASS = {
    2: Blind
}


class HomePilotAPI:
    """Class to communicate with the Rademacher HomePilot API."""

    def __init__(self, auth: Auth):
        """Initialize the API and store the auth so we can make requests."""
        self.auth = auth

    async def async_get_actuators(self) -> List[Actuator]:
        """Return all actuators."""
        resp_json = await self.auth.request("get", "v4/devices?devtype=actuator")
        return [ACTUATOR_CLASS[actuator_data["deviceGroup"]](actuator_data, self.auth) for actuator_data in resp_json["devices"]]

    async def async_get_all_devices(self) -> List[Device]:
        """Return all devices (currently only supporting actuators)."""
        return await self.async_get_actuators()

    async def async_get_system_name(self) -> str:
        """Return the system name."""
        resp_json = await self.auth.request("get", "service/system/networkmgr/v1/nodename")
        return resp_json["nodename"]
