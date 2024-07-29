from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
# import os
# import sys
from .. import models, schemas, oauth2
# srcdirectory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.insert(0, srcdirectory)
# import models, schemas, oauth2
from typing import Optional, List
from ..database import get_db
# from ..database import get_db
from sqlalchemy.orm import Session # type: ignore
from sqlalchemy import func # type: ignore


# func.count(models.Post.id).label('posts_count')

router = APIRouter(
    prefix= "/posts",
    tags= ['Posts']
)
@router.get("/", response_model= List[schemas.Post])
# @router.get("/")
def get_posts(db: Session = Depends(get_db), Limit: int = 5, skip: int = 0, search: Optional[str] = ""):
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(Limit).offset(skip).all()
    # cursor.execute("SELECT * FROM public.posts")
    # posts = cursor.fetchall()
    # print(posts)
    results = db.query(models.Post).join(models.User, models.Post.id == models.User.id, isouter = True).group_by(models.Post.id).all()
    # print(results)
    # return posts
    return results
@router.post("/", status_code = status.HTTP_201_CREATED, response_model= schemas.Post)
def create_post(post: schemas.CreatePost, db: Session = Depends(get_db)):
    post_created = models.Post(**post.model_dump())
    # print(current_user.id)
    # post_created = models.Post(title = post.title, body = post.body,  published = post.published)
    # print(post_created)
    db.add(post_created)
    db.commit()
    db.refresh(post_created)
    # cursor.execute("INSERT INTO public.posts (title, body, published) VALUES (%s, %s, %s) returning *", 
    #                (post.title, post.body, post.published))
    # new_post = cursor.fetchone()
    # connection.commit()
    
    
    # new_post = post.model_dump()
    # new_post['id'] = randrange(1, 100000)
    # my_posts.append(new_post)    
    # # print(post.rating)
    # print(new_post)
    return post_created

@router.get("/{id}", response_model= schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)):
    
    # get_one_post = db.query(models.Post).filter(models.Post.id == id).first()
    post = db.query(models.Post).join(models.User, models.Post.id == models.User.id, isouter = True).group_by(models.Post.id).filter(models.Post.id == id).first()
    # cursor.execute("select * from public.posts where id = %s", (str(id),))
    # post = cursor.fetchone()
    # post_found = find_post(id)
    # if not post:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with {id} not found"}
    return post


@router.delete("/{id}", status_code=204) 
def delete_post(id: int, db: Session = Depends(get_db)):
    post_deleted = db.query(models.Post).filter(models.Post.id == id)
    
    # cursor.execute("DELETE FROM public.posts WHERE id = %s", (str(id),))
    # deleted_post = cursor.fetchone()
    # connection.commit()    
    if post_deleted.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Given data not found")
    post_deleted.delete(synchronize_session = False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model= schemas.Post)
def update_post(id: int, post: schemas.CreatePost, db: Session = Depends(get_db)):
    update_query = db.query(models.Post).filter(models.Post.id == id)
    post = update_query.first()
    # cursor.execute("update public.posts set title = %s, body = %s, published = %s where id = %s", (post.title, post.body, post.published, str(id)))
    # index = find_index_post(id)
    # updated_post = cursor.fetchone()
    # connection.commit()
    if post == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"given data {id} not found")
    
    update_query.update({'title': 'title changed', 'body': 'and body also'}, synchronize_session = False)
    db.commit()
    # post_dict = post.model_dump()
    # post_dict["id"] = id
    # my_posts[index] = post_dict
    return post

