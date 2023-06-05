# importing from ../ folder and importing schemas, db models,
# oauth2 files and some utility files
from .. import schemas, models, utils, oauth2

# importing fastapi and its dependencies
# Using APIRouters to define router for POSTS
from fastapi import FastAPI, Depends, Response, status, HTTPException, APIRouter

# Gettng SQL Server and database dependencies
from sqlalchemy.orm import Session
from ..database import get_db




# Defining the route and tags for it.
# PREFIX_URL = /posts
# TAGS = POSTS
router = APIRouter(
    prefix="/posts",
    tags=["POSTS"]
)


# TestingGround for No AuthenticationPart 
@router.get("/sql")
def test_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts


# Get All the posts only if you have correct token and authentication
@router.get("/", response_model=list[schemas.Post])
async def get_post(db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    posts = db.query(models.Post).all()
    return posts




@router.post("/", status_code=201, response_model=schemas.Post)
async def create_postpayload(new_post: schemas.PostCreate, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    new_post = models.Post(
        **new_post.dict()
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post) 
    return new_post




# THE BOTTOM FUNCTION ONLY GIVES THE LATEST POST EVER POSTED
@router.get("/latest")
async def latest_post_by_id():
    return {
        "message": "You have been played nicely."
    }




# Function required proper authentication and should be able to het proper ID
# gETTING POST USING the ID of the post
@router.get("/{id}", response_model=schemas.Post)
async def get_post_by_id(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    posts = db.query(models.Post).filter(models.Post.id == id).first()
    if not posts:
        raise HTTPException(status_code=404, detail=f"Post id {id} not found")
    return posts



# delete specific id and all
# Requires proper authentication else will give error
@router.delete("/{id}", status_code=204)
async def delete_post_by_id(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=404, detail=f"Post id {id} not found")
    post.delete(synchronize_session=False)
    db.commit()

    # retunring only this message
    return {"data": "deleted_post"}


# UPDAETES THE code as per our wish
@router.put("/{id}")
async def update_post_by_id(id: int, postID: schemas.PostCreate, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=404, detail=f"Post id {id} not found")
    post.update(postID.dict(), synchronize_session=False)
    db.commit()
    db.refresh(post.first())
    return post.first()
