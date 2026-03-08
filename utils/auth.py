from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt,JWTError

SECRET_KEY="mysecretekey"
ALGORITHM="HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload=jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email=payload.get("sub")
        if not email:
            raise HTTPException(status_code=401, detail="invalid token")
        return email
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
