from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

# This file must exist before the endpoint is called.
FILE_PATH = Path(__file__).parent / "sample.txt"


@app.get("/download")
def download_file():
    return FileResponse(
        path=FILE_PATH,
        filename="sample.txt",
        media_type="text/plain",
    )
