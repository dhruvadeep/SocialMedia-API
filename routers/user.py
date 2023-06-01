from .. import schemas, models, utils
from fastapi import FastAPI, Depends, Response, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db


router = APIRouter(
    prefix="/users",
    tags=["USERS"]
)



# NEW USERS
@router.post("/", status_code=201, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate ,db: Session = Depends(get_db)):
    # return {"data": "User created"}
    
    # hashing the password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    
    
    
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user  
    
    


# Get users
@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User id {id} not found")
    return user
