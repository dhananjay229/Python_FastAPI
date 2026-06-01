from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user_model import User
from app.schemas.auth_schema import(
    SignupRequest,
    LoginRequest
)
from app.utils.token import (
    create_access_token,
    create_refresh_token
)
from app.core.security import (
    hash_password,
    verify_password
)

class AuthService:
    @staticmethod
    async def signup(
        payload: SignupRequest,
        db: AsyncSession
    ):
        existing_user = await db.scalar(
            select(User).where(User.email == payload.email)
        )

        if existing_user:
            raise Exception("User already exists")
        
        user = User(
            username=payload.username,
            email = payload.email,
            hashed_password=hash_password(payload.password)
        )

        db.add(user)
        await db.commit()
        await db.refresh(user)

        return user
    
    @staticmethod
    async def login(
        payload: LoginRequest,
        db: AsyncSession
    ):
        
        user = await db.scalar(
            select(User).where(User.email == payload.email)
        )
        
        if not user:
            return None
        
        if not verify_password(
            payload.password,
            user.hashed_password
        ):
            return None
        
        access_token = create_access_token(
            {"sub": str(user.id)}
        )

        refresh_token = create_refresh_token(
            {"sub": str(user.id)}
        )

        return{
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type":'bearer'
        }

