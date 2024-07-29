from fastapi import Response, status, HTTPException, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
# import os
# import sys
from .. import models, schemas, oauth2, utils
# srcdirectory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.insert(0, srcdirectory)
# import models, schemas, utils, oauth2
# from typing import Optional, List
from ..database import get_db
from sqlalchemy.orm import Session # type: ignore



router = APIRouter(
    tags= ['Users']
)




@router.post("/users", status_code=status.HTTP_201_CREATED, response_model= schemas.ShowUser)
def createuser(user:schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hashedUser(user.password)
    user.password = hashed_password
    user_created = models.User(**user.model_dump())
    db.add(user_created)
    db.commit()
    db.refresh(user_created)  

    return user_created

@router.post("/Users", status_code=status.HTTP_201_CREATED, response_model= schemas.ShowUser)
def createuser(user:schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hashedUser(user.password)
    
    user.password = hashed_password
    user_created = models.User(**user.model_dump())
    db.add(user_created)
    db.commit()
    db.refresh(user_created)  

    return user_created


@router.get("/users/{id}", response_model= schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    got_user = db.query(models.User).filter(models.User.id == id).first()
    
    if not got_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User with given {id} not found")
    
    return got_user


@router.post("/token")
def get_token(user_credentials: schemas.TokenData, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_credentials.id).first()
    getToken = oauth2.access_token(data={"user_id": user.id})
    print(user.id)
    return {"access_token": getToken, "token_type": "bearer"}
