import asyncio


async def main() -> None:
    print('Part one ...')
    await asyncio.sleep(1)
    print('... part two')

asyncio.run(main())
