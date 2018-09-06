import asyncio
import requests
import time
import aiohttp

#async def download(url):
#    print("get %s" % url)
#    response = requests.get(url)
#    print(response.status_code)

#async def wait_download(url):
#    await download(url)
#    print("get {} response complete.". format(url))

async def wait_download(url):
    print("get: %s" % url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)

async def main():
    start = time.time()
    await asyncio.wait([
        wait_download("http://www.qq.com"),
        wait_download("http://10.8.116.3"),
        wait_download("http://www.ctrip.com")
    ])
    end = time.time()
    print("Complete in {} senconds".format(end-start))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())