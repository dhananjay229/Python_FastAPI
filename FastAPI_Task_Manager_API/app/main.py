from fastapi import FastAPI
from app.routers.task_router import router as task_router

app = FastAPI(
    title = "Task Manager API",
    description = "Create a FastAPI Task Manager",
    version = "1.0.0"
)

app.include_router(task_router)

