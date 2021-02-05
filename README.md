# Rademacher HomePilot Python Package
Python package for communicating with the Rademacher HomePilot API.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install homepilot.

```bash
pip install homepilot
```

### Requirements

This package also requires [aiohttp](https://docs.aiohttp.org/en/stable/).

```bash
pip install aiohttp
```

## Usage

```python
import asyncio
import aiohttp

from homepilot import HomePilotAPI
from homepilot.auth import Auth


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