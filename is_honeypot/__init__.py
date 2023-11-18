from typing import Optional

import aiohttp

from .models import Response


class IsHoneypot:
    def __init__(self, session: Optional[aiohttp.ClientSession] = None):
        self.session = session or aiohttp.ClientSession()

    async def is_honeypot(self, address: str) -> Response:
        resp = await self.session.get(
            f"https://api.honeypot.is/v2/IsHoneypot?address={address}"
        )
        resp = await resp.json()

        if "error" in resp:
            raise Exception(resp["error"])
        return Response(**resp)

    async def close(self):
        await self.session.close()


async def is_honeypot(address: str) -> Response:
    hp = IsHoneypot()
    result = await hp.is_honeypot(address=address)
    await hp.close()
    return result
