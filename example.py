import asyncio
import aiohttp

from pyhomepilot import HomePilotAPI
from pyhomepilot.auth import Auth


async def main():
    async with aiohttp.ClientSession() as session:
        auth = Auth(session, "http://192.168.1.10", "password-if-configured")
        # only if a password is configured
        await auth.async_login()
        
        api = HomePilotAPI(auth)

        devices = await api.async_get_all_devices()
        print([device.name for device in devices])
        

asyncio.run(main())