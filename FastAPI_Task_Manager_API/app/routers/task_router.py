from fastapi import APIRouter, HTTPException, Query,status
from typing import List, Optional
from app.schema.task_schema import (
    TaskCreate,
    TaskResponse,
    TaskUpdate
)
from app.services.task_services import TaskService

router = APIRouter(
    prefix = "/tasks",
    tags=["Tasks"]
)

@router.post(
    "/",
    response_model = TaskResponse,
    status_code = status.HTTP_201_CREATED
)
def create_task(task: TaskCreate):
    return TaskService.create_task(task)

@router.get(
    "/",
    response_model=List[TaskResponse]
)
def get_tasks(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    completed: Optional[bool] = None
):
    return TaskService.get_tasks(
        skip=skip,
        limit=limit,
        completed=completed
    )

@router.get(
    "/{task_id}",
    response_model=TaskResponse
)
def get_task(task_id: int):

    task = TaskService.get_task_by_id(task_id)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return task


@router.put(
    "/{task_id}",
    response_model=TaskResponse
)
def update_task(task_id: int, task: TaskUpdate):

    updated_task = TaskService.update_task(task_id, task)

    if not updated_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return updated_task


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_task(task_id: int):

    deleted_task = TaskService.delete_task(task_id)

    if not deleted_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return None
