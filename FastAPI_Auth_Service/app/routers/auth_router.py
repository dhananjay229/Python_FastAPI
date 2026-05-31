from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.auth_schema import (
    SignupRequest,
    LoginRequest,
    TokenResponse
)
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/signup")
async def signup(
    payload: SignupRequest,
    db: AsyncSession = Depends(get_db)
):
    return await AuthService.signup(payload, db)

@router.post(
    "/login",
    response_model=TokenResponse
    )
async def login(
    payload: LoginRequest,
    db: AsyncSession = Depends(get_db)
):
    tokens = await AuthService.login(payload, db)

    if not tokens:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    
    return tokens

