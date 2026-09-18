from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...),
):
    return {
        "username": username,
        "message": "Form data received",
        "password_was_provided": bool(password),
    }
