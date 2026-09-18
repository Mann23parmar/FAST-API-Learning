import asyncio

from fastapi import FastAPI

app = FastAPI()


async def get_message():
    # await pauses this function while the work is in progress.
    await asyncio.sleep(1)
    return "The async task is complete"


@app.get("/message")
async def read_message():
    message = await get_message()
    return {"message": message}
