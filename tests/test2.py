import aiohttp
import asyncio
from sandclock import sandclock


async def status(session: aiohttp.ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status


@sandclock(2, 3, True)
async def f2():
    async with aiohttp.ClientSession() as session:
        urls = ['https://google.com', 'xxx://bad-request.com']
        tasks = [status(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        exceptions = [res for res in results if isinstance(res, Exception)]
        successful_results = [res for res in results if not isinstance(res, Exception)]

        print(f'All results: {results}')
        print(f'Finished successfully: {successful_results}')
        print(f'Threw exceptions: {exceptions}')

asyncio.run(f2())
