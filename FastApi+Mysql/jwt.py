from fastapi import FastAPI, HTTPException
from jose import jwt

app = FastAPI()

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"


@app.post("/login")
def login():
    data = {
        "username": "manan"
    }

    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return {"access_token": token}


@app.get("/profile")
def profile(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload["username"]

        return {
            "message": f"Welcome {username}"
        }

    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )