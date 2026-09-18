from fastapi import FastAPI

app = FastAPI(
    title="Student Management API",
    description="API for managing student records",
    version="1.0.0"
)

@app.get(
    "/students",
    summary="Get all students",
    description="Returns a list of all students."
)
def get_students():
    return {"message": "All students"}




