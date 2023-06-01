# importing the FastAPI class from the fastapi module
from fastapi import FastAPI, Depends, Response, status, HTTPException
# importing the BaseModel class from the pydantic module
from pydantic import BaseModel
# importing the typing module
from typing import Optional
from random import randint

# PGSQL imports
from psycopg2.extras import RealDictCursor
import time
import psycopg2

# SQLAlchemy imports
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db

from .routers import post, user

# Its used to create the database if it doesn't exist or connects the database if it exists
models.Base.metadata.create_all(bind=engine)








app = FastAPI()


app.include_router(post.router)
app.include_router(user.router)



