from fastapi import FastAPI

app = FastAPI(
    title="Beginner Swagger UI API",
    description="Open /docs to try the interactive Swagger UI.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.get("/hello")
def hello():
    return {"message": "Open /docs for Swagger UI"}
