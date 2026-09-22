from fastapi import APIRouter, FastAPI

app = FastAPI()
student_router = APIRouter(prefix="/students", tags=["students"])


@student_router.get("/")
def list_students():
    return [{"name": "Asha", "course": "FastAPI"}]


@student_router.get("/{student_id}")
def get_student(student_id: int):
    return {"id": student_id, "name": "Asha"}


app.include_router(student_router)
