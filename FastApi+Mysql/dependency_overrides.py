from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient

app = FastAPI()


def get_database():
	return "Real Database"


@app.get("/")
def home(db=Depends(get_database)):
	return {"database": db}


def fake_database():
	return "Fake Database"


app.dependency_overrides[get_database] = fake_database

client = TestClient(app)

response = client.get("/")

print(response.json())
