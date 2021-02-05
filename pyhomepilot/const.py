from enum import Enum


class DeviceGroup(Enum):
    BLIND = 2


# Commands
POS_UP_CMD = "POS_UP_CMD"
POS_DOWN_CMD = "POS_DOWN_CMD"
STOP_CMD = "STOP_CMD"
GOTO_POS_CMD = "GOTO_POS_CMD"
SET_SLAT_POS_CMD = "SET_SLAT_POS_CMD"
INC_CMD = "INC_CMD"
DEC_CMD = "DEC_CMD"