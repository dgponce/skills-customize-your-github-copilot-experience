import asyncio

async def worker(name, delay):
    await asyncio.sleep(delay)
    return f"{name} done"

async def main():
    results = await asyncio.gather(worker('A', 1), worker('B', 2))
    print(results)

if __name__ == '__main__':
    asyncio.run(main())
