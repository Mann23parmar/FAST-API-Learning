from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
STATIC_DIRECTORY = Path(__file__).parent / "static"
STATIC_DIRECTORY.mkdir(exist_ok=True)

app.mount("/static", StaticFiles(directory=STATIC_DIRECTORY), name="static")


@app.get("/")
def home():
    return {"message": "Open /static/example.txt to serve a static file"}
