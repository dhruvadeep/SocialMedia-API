from .database import Base
from sqlalchemy import Column, Integer, String, Boolean,text
from sqlalchemy.sql.sqltypes import TIMESTAMP

# MODELS
# creating models
# Creating modules for SQLAlchemy or any ORM framework simplifies the usage of the framework, improves code organization, promotes  
# code reuse, allows customization, facilitates testing, and enables performance optimizations.
# done by sachin

# Creating models for POSTS table
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, server_default="TRUE")
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))

# Creating models for USERS table
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    email = Column(String, primary_key=True,unique=True ,nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
