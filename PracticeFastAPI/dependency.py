from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


def get_current_user():
    return {"username": "manan", "is_active": True}


CurrentUser = Annotated[dict, Depends(get_current_user)]


@app.get("/profile")
def profile(user: CurrentUser):
    return {"user": user}
