from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class TaskBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=100)
    completed: bool = False
    due_date: Optional[date] = None
    priority: int  = Field(..., ge=1, le=5)

class TaskCreate(TaskBase):
    pass 

class TaskUpdate(BaseModel):
    title:Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=100)
    completed: Optional[bool] = None
    due_date :Optional[date] = None
    priority: Optional[int] = Field(None, ge=1, le=5)

class TaskResponse(TaskBase):
    id : int
    

