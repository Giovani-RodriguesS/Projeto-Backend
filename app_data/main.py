from fastapi import FastAPI
from src.routes import route

app = FastAPI()

app.include_router(route)

