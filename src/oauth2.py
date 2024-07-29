import jwt # type: ignore
from datetime import datetime, timedelta, timezone
from jwt.exceptions import InvalidTokenError # type: ignore
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from . import models, schemas
from sqlalchemy.orm import Session # type: ignore
from .database import get_db
from .config import settings

oauth_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def access_token(data: dict):
    
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
    
    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:
        breakpoint()
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)
    
    except InvalidTokenError:
        print("Invalid token, raising credentials_exception")
        raise credentials_exception
    
    return token_data

def get_current_user(token: str = Depends(oauth_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= f"could not authenticate credentials", 
                                         headers= {"www-authenticate": "Bearer"} )
    
    token =  verify_access_token(token, credentials_exception)
    
    user = db.query(models.User).filter(models.User.id == token.id).first()

    return user


    
    
