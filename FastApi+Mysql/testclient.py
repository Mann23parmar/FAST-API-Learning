from fastapi import FastAPI
from fastapi.testclient import TestClient
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}
client=TestClient(app)
response=client.get("/")
print(response.status_code)
print(response.json())
