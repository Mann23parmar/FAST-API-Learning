from pathlib import Path

from fastapi import BackgroundTasks, FastAPI

app = FastAPI()
LOG_FILE = Path(__file__).parent / "background_log.txt"


def write_log(message: str):
    with LOG_FILE.open("a", encoding="utf-8") as file:
        file.write(message + "\n")


@app.post("/send-email")
def send_email(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, "Email task completed")
    return {"message": "The background task was scheduled"}
