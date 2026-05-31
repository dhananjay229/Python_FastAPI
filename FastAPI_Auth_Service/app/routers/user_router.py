from fastapi import APIRouter, Depends
from app.dependencies.auth_dependency import (
    get_admin_user,
    get_current_user
)
from app.models.user_model import User

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/me")
async def get_me(
    current_user : User = Depends(get_current_user)
):
    return current_user

@router.get("/admin")
async def admin_dashboard(
    admin: User = Depends(get_admin_user)
):
    return {
        "message": "Welcome Admin"
    }

