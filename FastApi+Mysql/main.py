import os

from dotenv import load_dotenv

load_dotenv()
import mysql.connector

from fastapi import FastAPI,HTTPException,Query,UploadFile,File,Depends
from pydantic import BaseModel
from typing import List
app = FastAPI()

# class StudentResponse(BaseModel):
    
#     name: str
#     age: int
#     course: str
    
    
# MySQL connection
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Manan@1234",
#     database="student_db"
# )
# db = mysql.connector.connect(
    
# )
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
cursor = db.cursor(dictionary=True)


# Pydantic model
class Student(BaseModel):
    name: str
    age: int
    course: str
    city: str


# POST - Create student
@app.post("/students")
def create_student(student: Student):

    query = """
        INSERT INTO students (name, age, course, city)
        VALUES (%s, %s, %s, %s)
    """

    values = (
        student.name,
        student.age,
        student.course,
        student.city
    )

    cursor.execute(query, values)

    db.commit()

    return {
        "message": "Student created successfully",
        "id": cursor.lastrowid
    }


# GET - Get all students
# @app.get("/students",response_model=List[StudentResponse])
@app.get("/students")
def get_students(city: str | None = Query(default=None)):

    if city:
        query = "SELECT * FROM students WHERE city = %s"
        cursor.execute(query, (city,))
    else:
        query = "SELECT * FROM students"
        cursor.execute(query)

    students = cursor.fetchall()

    return students

# GET - Get one particular student
@app.get("/students/{student_id}")
def get_student(student_id: int):

    query = "SELECT * FROM students WHERE id = %s"

    cursor.execute(query, (student_id,))

    student = cursor.fetchone()

    if student is None:
        raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
    else:
        return student


# PUT - Update student
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):

    query = """
        UPDATE students
        SET name = %s,
            age = %s,
            course = %s,
            city = %s
        WHERE id = %s
    """

    values = (
        student.name,
        student.age,
        student.course,
        student.city,
        student_id
    )

    cursor.execute(query, values)

    db.commit()

    if cursor.rowcount == 0:
        return {"message": "Student not found"}

    return {
        "message": "Student updated successfully"
    }


# DELETE - Delete student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    query = "DELETE FROM students WHERE id = %s"

    cursor.execute(query, (student_id,))

    db.commit()

    if cursor.rowcount == 0:
        return {"message": "Student not found"}

    return {
        "message": "Student deleted successfully"
    }

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    return {
        "filename": file.filename
    }


# dependency example
def check_user():
    return "User verified"

@app.get("/students123")
def get_students(user=Depends(check_user)):
    return {
        "message": "Students fetched",
        "user": user
    }