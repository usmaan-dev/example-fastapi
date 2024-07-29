from fastapi import Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, oauth2, database
from sqlalchemy.orm import Session # type: ignore

router = APIRouter(
    prefix= "/votes",
    tags= ['Votes']
)

@router.post("/", status_code = status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db)):
    
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Post with id {vote.post_id} not found")
    
    vote_query = db.query(models.Votes).filter(models.Votes.post_id == vote.post_id, models.Votes.user_id == vote.user_id)
    vote_found = vote_query.first()
    
    
    if vote.dir == 1:
        if vote_found:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= f"User with id {vote.user_id} has already voted for post with id {vote.post_id}")
        new_vote = models.Votes(post_id = vote.post_id, user_id = vote.user_id)
        db.add(new_vote)
        db.commit()
        return {"message": "Vote added successfully"}
    else:
        if not vote_found:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User with id {vote.user_id} has not voted for post with id {vote.post_id}")
        
        vote_query.delete(synchronize_session=False)
        
        return {"message": "Vote removed successfully"}