# (c) 2022-2023, Akkil MG
# License: GNU General Public License v3.0

import asyncio
import time
from helpers.g_login import g_login

async def main():
    print('------------------- Testing -------------------')
    print('----------------------- Service Started -----------------------')
    try:
        while True:
            auth = await g_login()
    except Exception as e:
        print(f"Exception occurred (main): {e}")
        return

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('----------------------- Service Stopped -----------------------')