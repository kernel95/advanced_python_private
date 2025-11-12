# api_async_investigation.py

import asyncio
import time
import httpx
from tqdm.asyncio import tqdm

#await needed to wait to event happening before proceeding
async def fetch(client, url):
    response = await client.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

#u2588 is like a progress bar
async def progress():
    for i in range(30):
        print(f"\u2588", end="", flush=True)
        await asyncio.sleep(0.25)
        
async def tqdm_progress(seconds):
    with tqdm(total=seconds, desc="Downloading...", unit="s") as pbar:
        for i in range(seconds):
            await asyncio.sleep(0.25)
            pbar.update(1)

#async means parallel execution
async def main():
    async with httpx.AsyncClient() as client:
        t1 = asyncio.create_task(fetch(client, "https://api.acodingtutor.com/members/5?_delay=2000"))
        t2 = asyncio.create_task(fetch(client, "https://api.acodingtutor.com/members/5?_delay=3000"))
        t3 = asyncio.create_task(tqdm_progress(10))
        
        r1,r2, _ = await asyncio.gather(t1, t2, t3)
        print("\n")
        print(r1)
        print(r2)


start_time = time.time()
asyncio.run(main())
end_time = time.time()

print(f"timet taken: {end_time - start_time}")