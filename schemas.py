from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# Base model for all the models (POSTS)
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

# Its base model for creating Posts
class PostCreate(PostBase):
    pass

# Its base model for updating Posts
# It inherits PostBase
class Post(PostBase):
    id: int
    created_at: datetime
    class Config():
        orm_mode = True




# USERS

# Base model for all the models (USERS)
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Its base model for creating Users
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config():
        orm_mode = True

# Its base model for LOGIN
class UserLogin(BaseModel):
    email: EmailStr
    password: str




# OAUTH2 SCHEMAS

# Base model for all the models (OAUTH2)
class Token(BaseModel):
    access_token: str
    token_type: str

# Its base model for creating Token AND VALIDING data
class TokenData(BaseModel):
    id: Optional[str] = None