from .. import schemas, models, utils
from fastapi import FastAPI, Depends, Response, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db


router = APIRouter(
    prefix="/posts",
    tags=["POSTS"]
)




@router.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts











@router.get("/")
async def root():
    return "Welcome to my blog"

@router.get("/", response_model=list[schemas.Post])
async def get_post(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    # print(posts)

    posts = db.query(models.Post).all()
    return posts




@router.post("/", status_code=201, response_model=schemas.Post)
async def create_postpayload(new_post: schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute(
    #     """INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",
    #             (new_post.title, new_post.content, new_post.published)
    #             )
    # post_dict = cursor.fetchone()
    # conn.commit()
    new_post = models.Post(
        **new_post.dict()
        # title=new_post.title,
        # content=new_post.content,
        # published=new_post.published
    )
    # db.add(new_post)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post







@router.get("/latest")
async def latest_post_by_id():
    cursor.execute("""SELECT * FROM posts ORDER BY id DESC LIMIT 1""")
    post = cursor.fetchone()
    return post










@router.get("/{id}", response_model=schemas.Post)
async def get_post_by_id(id: int, db: Session = Depends(get_db)):
    posts = db.query(models.Post).filter(models.Post.id == id).first()
    if not posts:
        raise HTTPException(status_code=404, detail=f"Post id {id} not found")
    return posts
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id),))
    # post = cursor.fetchone()
    # if not post:
    #     raise HTTPException(status_code=404, detail=f"Post id {id} not found")
    # # raise HTTPException(status_code=404, detail=f"Post id {id} not found")
    # return {"data": post}











@router.delete("/{id}", status_code=204)
async def delete_post_by_id(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=404, detail=f"Post id {id} not found")
    post.delete(synchronize_session=False)
    db.commit()
    return {"data": "deleted_post"}









@router.put("/{id}")
async def update_post_by_id(id: int, postID: schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (postID.title, postID.content, postID.published, str(id)))
    # post = cursor.fetchone()
    # conn.commit()
    post = db.query(models.Post).filter(models.Post.id == id)

    if not post.first():
        raise HTTPException(status_code=404, detail=f"Post id {id} not found")
    post.update(postID.dict(), synchronize_session=False)
    db.commit()
    db.refresh(post.first())
    return post.first()
