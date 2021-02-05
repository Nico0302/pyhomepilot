from pyhomepilot.const import (
    POS_UP_CMD,
    POS_DOWN_CMD,
    STOP_CMD,
    GOTO_POS_CMD,
    SET_SLAT_POS_CMD,
    INC_CMD,
    DEC_CMD
)
from .actuator import Actuator


class Blind(Actuator):
    """Class that represents an Blind object in the HomePilot API."""

    def __init__(self, *args, **kwargs):
        """Initialize an blind object."""
        super(Blind, self).__init__(*args, **kwargs)

    @property
    def slatposition(self) -> int:
        """Return the slatposition of the blind (only if supported)."""
        if not "slatposition" in self.statusMap:
            return None
        return self.statusMap["slatposition"]

    async def async_move_up(self):
        """Send up command to the blind."""
        await self.async_command(POS_UP_CMD)

    async def async_move_down(self):
        """Send down command to the blind."""
        await self.async_command(POS_DOWN_CMD)

    async def async_stop(self):
        """Send stop command to the blind."""
        await self.async_command(STOP_CMD)

    async def async_goto_position(self, position: int):
        """Send goto position command to the blind."""
        await self.async_command(GOTO_POS_CMD, position)

    async def async_set_saltposition(self, position: int):
        """Send set salt position command to the blind."""
        await self.async_command(SET_SLAT_POS_CMD, position)

    async def async_inc_saltposition(self):
        """Send increment position command to the blind."""
        await self.async_command(INC_CMD)

    async def async_dec_saltposition(self):
        """Send increment position command to the blind."""
        await self.async_command(DEC_CMD)
    