from fastapi import HTTPException
from models.userModel import User
from utils.hash import hash_password, verify_password
from utils.jwt import create_access_token

def signin_user(user,db):
    newUser=User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    token=create_access_token({"sub": newUser.email})
    return {"user": {"id": newUser.id, "name": newUser.name, "email": newUser.email}, "token": token}

def signup_user(user,db):
    existUser=db.query(User).filter(User.email==user.email).first()
    if not existUser:
        raise HTTPException(status_code=404, detail="user not found")
    if not verify_password(user.password, existUser.password):
        raise HTTPException(status_code=400, detail="invalid password")
    token=create_access_token({"sub": existUser.email})
    return {"user": {"id": existUser.id, "name": existUser.name, "email": existUser.email}, "token": token}

def get_user_by_email(email,db):
    user=db.query(User).filter(User.email==email).first()
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return {"id": user.id, "name": user.name, "email": user.email}
