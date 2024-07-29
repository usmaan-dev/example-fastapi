from sqlalchemy import Column, Integer, String, Boolean, ForeignKey # type: ignore
from sqlalchemy.sql.sqltypes import TIMESTAMP # type: ignore
from sqlalchemy.sql.expression import text # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from .database import Base


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key = True, nullable = False)
    title = Column(String, nullable = False)
    body = Column(String, nullable = False)
    published = Column(Boolean, server_default = 'True')
    created_at = Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))
    # owner_id = Column(Integer, ForeignKey('Users.id', ondelete = 'CASCADE'), nullable = False)
    # owner = relationship("User") 
    
    
class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, nullable = False, primary_key = True)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
    created_at = Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))
    

class Votes(Base):
    __tablename__ = "Votes"
    post_id = Column(Integer, ForeignKey('posts.id', ondelete = 'CASCADE'), primary_key = True)
    user_id = Column(Integer, ForeignKey('Users.id', ondelete = 'CASCADE'), primary_key = True)