import asyncio
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


async def generate_messages() -> AsyncGenerator[str, None]:
    for number in range(1, 4):
        yield f"Message {number}\n"
        await asyncio.sleep(1)


@app.get("/stream")
def stream_messages():
    return StreamingResponse(
        generate_messages(),
        media_type="text/plain",
    )
