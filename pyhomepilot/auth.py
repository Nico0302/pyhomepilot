from http.cookies import SimpleCookie
from aiohttp import ClientSession, ClientResponse, ClientConnectorError, ClientResponseError
from .utils import sha256hex, format_url


class Auth:
    """Class to make authenticated requests."""

    def __init__(self, websession: ClientSession, host: str, password: str=None, auth_cookies: SimpleCookie=None):
        """Initialize the auth."""
        self.websession = websession
        self.host = format_url(host)
        self.password = password
        self.auth_cookies = auth_cookies

    async def async_login(self) -> ClientResponse:
        """Require auth cookies."""
        if self.password == None:
            return None

        try:
            salt_resp = await self.raw_request("post", "authentication/password_salt")
            salt_json = await salt_resp.json()
            salt_resp.raise_for_status()
            salt = salt_json["password_salt"]
            payload = {
                'password': sha256hex(salt + sha256hex(self.password)),
                'password_salt': salt
            }
            resp = await self.raw_request("post", "authentication/login", json=payload)
            resp_json = await resp.json()
            resp.raise_for_status()
            self.auth_cookies = resp.cookies
            return resp
        except ClientConnectorError as err:
            raise ConnectionError(*err.args)
        except ClientResponseError as err:
            err_json = resp_json if "resp_json" in locals() else salt_json
            raise AuthError(message=err_json["error_description"], *err.args)

    async def async_logout(self) -> ClientResponse:
        """Logout from pyhomepilot."""
        resp = await self.request("post", "authentication/logout")
        await self.websession.close()
        return resp

    async def raw_request(self, method: str, path: str, **kwargs) -> ClientResponse:
        """Make a basic request."""
        headers = kwargs.get("headers")

        if headers is None:
            headers = {}
        else:
            headers = dict(headers)

        try:
            resp = await self.websession.request(
                method, f"{self.host}/{path}", **kwargs, headers=headers, cookies=self.auth_cookies
            )
        except ClientConnectorError as err:
            raise ConnectionError(*err.args)
        else:
            return resp

    async def request(self, *args, reauthenticate=True, **kwargs) -> dict:
        """Make a request with json parsing and reauthentication."""
        try:
            resp = await self.raw_request(*args, **kwargs)
            resp_json = await resp.json()
            resp.raise_for_status()
        except ClientResponseError as err:
            message = resp_json["error_description"] if "resp_json" in locals() else await resp.text()

            if err.status == 401 or (message == "Unauthorized"):
                if reauthenticate and (self.password != None):
                    await self.async_login()
                    return await self.request(*args, reauthenticate=False, **kwargs)
                raise AuthError(message=message, *err.args) 

            raise ResponseError(message=message, *err.args)
        else:
            return resp_json
                

class ConnectionError(ClientConnectorError):
    """Error to indicate we cannot connect."""

class ResponseError(ClientResponseError):
    """Error to indicate a general error with the request or the server."""

class AuthError(ClientResponseError):
    """Error to indicate there is invalid auth."""