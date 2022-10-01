import enum

import aiohttp

from .models import Response


class Chain(str, enum.Enum):
    ETH = "eth"
    BSC = "bsc2"


class IsHoneypot:
    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def is_honeypot(self, chain: Chain, token: str) -> Response:
        resp = await self.session.get(
            f"https://aywt3wreda.execute-api.eu-west-1.amazonaws.com/default/"
            f"IsHoneypot?chain={chain}&token={token}"
        )
        resp = await resp.json()
        if resp.get("IsHoneypot") is None:
            await self.close()
            raise Exception(resp["message"])
        return Response(**resp)

    async def close(self):
        await self.session.close()


async def is_honeypot(chain: Chain, token: str) -> Response:
    hp = IsHoneypot()
    result = await hp.is_honeypot(chain, token)
    await hp.close()
    return result
