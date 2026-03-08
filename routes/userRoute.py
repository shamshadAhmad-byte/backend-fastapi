from fastapi import APIRouter, Depends, HTTPException
from schemas.userSchema import UserIn, UserOut, UserResponse, AuthResponse
from controller.userController import signin_user, signup_user, get_user_by_email
from config.db import engine, get_db, Base
from models.userModel import User
from sqlalchemy.orm import Session

from utils.hash import verify_password
from utils.auth import get_current_user

# Base.metadata.create_all(bind=engine)

userRouter=APIRouter()

@userRouter.post("/user/register", response_model=AuthResponse, status_code=201)
async def register(user: UserIn, db: Session=Depends(get_db)):
    if db.query(User).filter(User.email==user.email).first():
        raise HTTPException(status_code=400, detail="email already exists")

    return signin_user(user, db)

@userRouter.post('/user/login', response_model=AuthResponse, status_code=200)
def login(user: UserOut, db: Session=Depends(get_db)):
    existUser=db.query(User).filter(User.email==user.email).first()
    if not existUser:
        raise HTTPException(status_code=404, detail="user not found")
    if not verify_password(user.password, existUser.password):
        raise HTTPException(status_code=401, detail="invalid password")
    return signup_user(user, db)

@userRouter.get("/user/profile", response_model=UserResponse, status_code=200)
def get_user(email: str=Depends(get_current_user), db: Session= Depends(get_db)):
    user=get_user_by_email(email,db)
    return user