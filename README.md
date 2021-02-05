# pyhomepilot
Python package for communicating with the Rademacher HomePilot API.

## Disclaimer

HomePilot is a trademark of the Rademacher company. Rademacher is not affiliated with the author or this project in any way.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pyhomepilot.

```bash
pip install pyhomepilot
```

## Usage

```python
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
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)