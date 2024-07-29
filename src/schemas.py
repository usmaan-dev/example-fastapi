from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from pydantic.types import conint


class PostBase(BaseModel):
    
    title: str
    body: str

    # rating: Optional[float] = None
  
 

class CreatePost(PostBase):
    id: int
    pass   

class ShowUser(BaseModel):
    email: EmailStr
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

class Post(PostBase):
    id: int
    created_at: datetime
    published: bool = True
    class Config:
        from_attributes = True



class UserCreate(BaseModel):
    email: EmailStr
    password: str
    



class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[str] = None
    

class Vote(BaseModel):
    post_id: int
    user_id: int
    dir: conint(le=1) # type: ignore
    
    
















# class CreatePost(BaseModel):
#     title: str
#     body: str
#     published: bool = True
#     # rating: Optional[float] = None
    
# class UpdatePost(BaseModel):
#     title: str
#     body: str
#     published: bool