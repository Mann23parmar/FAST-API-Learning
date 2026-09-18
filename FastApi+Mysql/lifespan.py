from contextlib import asynccontextmanager
from fastapi import FastAPI
@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Connecting to database...")
    
    yield
    
    print("Closing database connection...")


app = FastAPI(lifespan=lifespan)

