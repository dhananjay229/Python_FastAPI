from app.database.db import task_db
from app.schema.task_schema import TaskCreate, TaskUpdate

class TaskService:

    @staticmethod
    def create_task(task:TaskCreate):
        task_data = task.model_dump()

        new_task = {
            "id": len(task_db) + 1,
            **task_data
        }

        task_db.append(new_task)
        return new_task
    
    @staticmethod
    def get_tasks(
        skip:int = 0,
        limit: int = 0,
        completed : bool | None = None
    ):
        filtered_task = task_db

        if completed is not None:
            filtered_task = [
                task for task in filtered_task
                if task["completed"] == completed
            ]

        return filtered_task[skip: skip + limit]
    
    @staticmethod
    def get_task_by_id(task_id:int):

        for task in task_db:
            if task["id"] == task_id:
                return task
            
        return None
    
    @staticmethod
    def update_task(task_id: int, task: TaskUpdate):

        existing_task = TaskService.get_task_by_id(task_id)

        if not existing_task:
            return None
        
        update_data = task.model_dump(exclude_unset = True)

        for key, value in update_data.items():
            existing_task[key] = value

        return existing_task
    
    @staticmethod
    def delete_task(task_id:int):

        for index, task in enumerate(task_db):

            if task["id"] == task_id:
                deleted_task = task_db.pop(index)
                return deleted_task
            
        return None




