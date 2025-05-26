import asyncio


await asyncio.sleep(10, result='hello')

async def main():
    await asyncio.sleep(1)
    print('hello')

with asyncio.Runner() as runner:
    runner.run(main())

    