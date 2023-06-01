from pydantic import BaseModel, EmailStr
from datetime import datetime

# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True

# class CreatePost(BaseModel):
#     title: str
#     content: str
#     published: bool = True

# class UpdatePost(BaseModel):
#     title: str
#     content: str
#     published: bool = True

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

# class PostUpdate(PostBase):
#     pass

# This i because we dont need id and all
class Post(PostBase):
    id: int
    # title: str
    # content: str
    # published: bool
    created_at: datetime
    class Config():
        orm_mode = True



class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    email: EmailStr
    created_at: datetime
    class Config():
        orm_mode = True