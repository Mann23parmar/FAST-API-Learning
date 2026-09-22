from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class StudentInput(BaseModel):
    name: str
    age: int
    course: str


class StudentResponse(BaseModel):
    name: str
    course: str


@app.post("/students", response_model=StudentResponse)
def create_student(student: StudentInput):
    # The response_model hides the age field from the response.
    return student
