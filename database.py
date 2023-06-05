# importing sqlalchemy and creating database engine and session
from sqlalchemy import create_engine
# importing declarative_base for creating base class
from sqlalchemy.ext.declarative import declarative_base
# importing sessionmaker for creating session
# sessionmaker is a class
from sqlalchemy.orm import sessionmaker

# DATABASE URL
# postgresql://user:password@host:port/database
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:A3AEB546@localhost/fastapi"

# create engine for database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create base
Base = declarative_base()

# define a function to get database
# function to do query imto database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()