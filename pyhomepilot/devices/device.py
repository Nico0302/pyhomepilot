from pyhomepilot.auth import Auth


class Device:
    """Class that represents a Device object in the HomePilot API."""

    def __init__(self, raw_data: dict, auth: Auth):
        """Initialize a device object."""
        self.raw_data = raw_data
        self.auth = auth

    @property
    def did(self) -> int:
        """Return the DID of the device."""
        return self.raw_data["did"]

    @property
    def uid(self) -> str:
        """Return the UID of the device."""
        return self.raw_data["uid"]

    @property
    def name(self) -> str:
        """Return the display name of the device."""
        return self.raw_data["name"]

    @property
    def description(self) -> str:
        """Return the description of the device."""
        return self.raw_data["description"]

    @property
    def statusMap(self) -> dict:
        """Return the status map of the device."""
        return self.raw_data["statusesMap"]

    @property
    def statusValid(self) -> dict:
        """Return if the staus is valid."""
        return self.raw_data["statusValid"]

    @property
    def properties(self) -> dict:
        """Return the properties of the device."""
        return self.raw_data["properties"]

    @property
    def deviceNumber(self) -> int:
        """Return the device number of the device."""
        return self.raw_data["deviceNumber"]

    @property
    def origin(self) -> str:
        """Return the origin of the device."""
        return self.raw_data["origin"]

    @property
    def visible(self) -> bool:
        """Return if the device is visible."""
        return self.raw_data["visible"]

    @property
    def iconSet(self) -> dict:
        """Retrun the icon set name of the device."""
        return self.raw_data["iconSet"]

    @property
    def iconSetInverted(self) -> int:
        """Return if the icon set of the device is inverted (1) or not (0)."""
        return self.raw_data["iconSetInverted"]

    @property
    def inverted(self) -> bool:
        """Return if the icon set of the device is inverted as boolean."""
        return bool(self.raw_data["iconSetInverted"])

    @property
    def voiceControlledBy(self) -> str:
        """Return the name of the voice assistant of the device."""
        return self.raw_data["voiceControlledBy"]

    async def async_update(self):
        """Update the device data."""
        resp_json = await self.auth.request("get", f"v4/devices/{self.did}")
        self.raw_data = resp_json["device"]

        