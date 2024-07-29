from fastapi import APIRouter, Depends, Response, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session # type: ignore
# import os,sys
# srcdirectory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.insert(0, srcdirectory)
from .. import models, oauth2, database, utils, schemas

router = APIRouter(tags= ['Authentication'])

@router.post("/login")
def loginUser(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= "Invalid Credentials")
    
    if not utils.verify_password(user_credentials.password, user.password):
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= "Invalid Credentials")
     
    access_token = oauth2.access_token(data={"user_id": user.id})
    print(user.id)
     
    return{"access_token": access_token, "token_type": "bearer"}

    
    