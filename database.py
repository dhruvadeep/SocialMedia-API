from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE URL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:A3AEB546@localhost/fastapi"

# create engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create base
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()