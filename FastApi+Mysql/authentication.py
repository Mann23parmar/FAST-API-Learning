from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

app = FastAPI()
security = HTTPBearer()


@app.get("/private")
def private_page(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
):
    if credentials.credentials != "beginner-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"message": "Authentication successful"}
