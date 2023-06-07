# importing the fastapi library and its dependencies
from fastapi import FastAPI, Depends, Response, status, HTTPException

# importing the BaseModel class from the pydantic module
# model is used for the validation of the data
# validation of sql and its datatypes
from pydantic import BaseModel

# importing the typing module
from typing import Optional
from random import randint
import time

# PGSQL imports

# database cursors are required 
from psycopg2.extras import RealDictCursor
import psycopg2

# SQLAlchemy imports
# Used for connecting to the database and query different sqls
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db



# Importing routers
# Routers are used to simplify different routes
from .routers import post, user, auth


# Its used to create the database if it doesn't exist or connects the database if it exists
models.Base.metadata.create_all(bind=engine)
"""
The above isnt required but provides more precious and correct sql.
Also removes sql vurnability
"""






# Calling the FastAPI
# Creates a small web server
app = FastAPI()

# Routers
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)



