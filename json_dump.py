import asyncio
import aiohttp
import json
from getpass import getpass

from pyhomepilot import HomePilotAPI
from pyhomepilot.auth import Auth, ConnectionError, AuthError


DEVICETYPES = {
    "Actuator",
    "Sensor",
    "Camera",
    "Transmitter"
}

FILENAME = "homepilot_dump.json"


async def async_fetch_data(auth):
    data = {}
    for devtype in DEVICETYPES:
            data[devtype] = await auth.request("get", f"v4/devices?devtype={devtype}")
    return data


def save_data(data):
    with open(FILENAME, "w") as outfile:
        json.dump(data, outfile)
    print(f"Saved data under '{FILENAME}'.")


async def main():
    data = {}

    async with aiohttp.ClientSession() as session:
        host = input("Hostname/IP: ")
        auth = Auth(session, host)

        try:
            auth = Auth(session, host)
            data = await async_fetch_data(auth)
        except ConnectionError:
            print(f"Host under '{host}' is not reachable!")
        except AuthError:
            try:
                auth.password = getpass(prompt="Password: ")
                data = await async_fetch_data(auth)
            except AuthError:
                print("Invalid password!")
            else:
                save_data(data)
        else:
            save_data(data)
        

asyncio.run(main())