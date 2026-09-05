import asyncio

async def makeCoffee():
    print("making coffee..")
    # after 3 min
    await asyncio.sleep(5)
    return "here is your coffee!"


async def makeTea():
    print("making TEa..")
    # after 3 min
    await asyncio.sleep(5)
    return "here is your Tea!"



async def main():
   tea  = makeTea()
   co = makeCoffee()
   await asyncio.gather(
        tea,co
    )
   

asyncio.run(main())