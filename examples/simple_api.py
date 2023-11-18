import asyncio

from is_honeypot import is_honeypot


async def main():
    resp = await is_honeypot(address="0x7e5521905Cd830E78A0a2B0F5a2748894A039282")
    print(resp)


asyncio.get_event_loop().run_until_complete(main())
