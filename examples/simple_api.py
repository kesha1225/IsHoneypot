import asyncio

from is_honeypot import is_honeypot, Chain


async def main():
    resp = await is_honeypot(Chain.BSC, "0x0641382232FC09B301fac7Fe165c3a28F6B5471c")
    print(resp)


asyncio.get_event_loop().run_until_complete(main())
