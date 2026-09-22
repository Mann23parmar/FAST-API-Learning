from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()


def get_current_user():
    # In a real app, this user would come from a validated token.
    return {"username": "manan", "role": "user"}


@app.get("/admin")
def admin_page(user=Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin permission required")
    return {"message": "Welcome to the admin page"}
