from fastapi import FastAPI
from pydantic import BaseModel, field_validator

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int

    @field_validator("name")
    @classmethod
    def name_must_not_be_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Name cannot be empty")
        return value.strip()

    @field_validator("age")
    @classmethod
    def age_must_be_valid(cls, value: int) -> int:
        if value < 5 or value > 100:
            raise ValueError("Age must be between 5 and 100")
        return value


@app.post("/students")
def create_student(student: Student):
    return {"message": "Student is valid", "student": student}
