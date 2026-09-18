from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

# This declares where a client can get an access token.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@app.post("/login")
def login():
    # A real application would check a username and password here.
    return {"access_token": "example-token", "token_type": "bearer"}


@app.get("/users/me")
def read_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
):
    return {
        "message": "This endpoint received an OAuth2 bearer token",
        "token": token,
    }
