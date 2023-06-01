from .database import Base
from sqlalchemy import Column, Integer, String, Boolean,text
from sqlalchemy.sql.sqltypes import TIMESTAMP

# create model
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, server_default="TRUE")
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    email = Column(String, primary_key=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
