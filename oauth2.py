from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from deps import get_db
import models
from jose import JWTError, jwt
import auth

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme),db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = auth.verify_access_token(token)
    if payload is None:
        raise credentials_exception
    
    user = db.query(models.User).filter(models.User.id == payload["id"]).first()
    if user is None:
        raise credentials_exception
    return user  # ✅ returns full user model
