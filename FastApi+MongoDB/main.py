from pymongo import MongoClient
from fastapi import FastAPI
from pydantic import BaseModel
from bson import ObjectId
app = FastAPI()

#db
client = MongoClient("mongodb://localhost:27017/")

db = client["student_db"]

students_collection = db["students"]

#pydantic
class Student(BaseModel):
    name: str
    age: int
    course: str
    city: str
    
@app.post("/students")
def create_student(student: Student):

    student_data = student.model_dump()

    result = students_collection.insert_one(student_data)

    return {
        "message": "Student created successfully",
        "id": str(result.inserted_id)
    }
    

# get all student
@app.get("/students")
def get_students():

    students = list(students_collection.find())

    for student in students:
        student["_id"] = str(student["_id"])

    return students


# get one particular student

@app.get("/students/{student_id}")
def get_student(student_id: str):

    student = students_collection.find_one(
        {"_id": ObjectId(student_id)}
    )

    if student is None:
        return {"message": "Student not found"}

    student["_id"] = str(student["_id"])

    return student


# update student

@app.put("/students/{student_id}")
def update_student(student_id: str, student: Student):

    result = students_collection.update_one(
        {"_id": ObjectId(student_id)},
        {"$set": student.model_dump()}
    )

    if result.matched_count == 0:
        return {"message": "Student not found"}

    return {
        "message": "Student updated successfully"
    }

@app.delete("/students/{student_id}")
def delete_student(student_id: str):

    result = students_collection.delete_one(
        {"_id": ObjectId(student_id)}
    )

    if result.deleted_count == 0:
        return {"message": "Student not found"}

    return {
        "message": "Student deleted successfully"
    }