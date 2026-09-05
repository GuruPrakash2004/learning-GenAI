import asyncio


# this is a syncrones function
async def countTime():
    print("count timer started")
    await asyncio.sleep(5)
    print("timer ended for counter")
async def callash():
    print("calling ash started")
    await asyncio.sleep(3)
    print("timer ended for calling")


async def main():
    await asyncio.gather(countTime(),callash())
   

if __name__ == "__main__":
   asyncio.run(main())
