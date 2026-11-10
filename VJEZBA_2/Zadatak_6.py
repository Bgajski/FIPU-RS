# za izvrsavanje korutine bez await task2 mozemo koristiti asyncio.sleep() unutar main

    # print("Fetch 1 uspješno završen.")

    # await asyncio.sleep(2)

    # return [result1]
    
import asyncio

async def fetch_data(param):
    print(f"Nešto radim s {param}...")
    await asyncio.sleep(param)
    print(f"Dovršio sam s {param}.")
    return f"Rezultat za {param}"

async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))

    await task1
    await asyncio.sleep(2)

asyncio.run(main())