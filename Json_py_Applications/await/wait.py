import time
from fastapi import FastAPI
import httpx
import asyncio


app = FastAPI()

url = "https://official-joke-api.appspot.com/random_joke"

@app.get("/joke-sync")
def getJock():
    start = time.time()
    joke = []

    with httpx.Client() as client:
        for _ in range(10):
            resp = client.get(url)
            data = resp.json()
            joke.append(f"{data["setup"] } - { data["punchline"] }")
    elapsed = time.time() - start


    return {
        "mode" :"sync",
        "elapsed_time" : round(elapsed,3),
        "jokes" : joke
    }


@app.get("/joke-assync")
async def getJock_async():
    start = time.time()
    joke = []

    async with httpx.AsyncClient() as client:
        task = [client.get(url) for _ in range(10)]
        resp = await asyncio.gather(*task)

        for res in resp:
            data = res.json()
            joke.append(f"{data["setup"] } - { data["punchline"] }")
    elapsed = time.time() - start


    return {
        "mode" :"sync",
        "elapsed_time" : round(elapsed,3),
        "jokes" : joke
    }





