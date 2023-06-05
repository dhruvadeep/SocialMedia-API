# UTILITIES functions for further use

# Importing libraries such as for creating JWT tokens, hashing passwords, etc.
# .Cryptograghy is used for creating JWT tokens
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Creating a hash for password
def hash(password: str):
    return pwd_context.hash(password)

# Verifying password and hashed password
def verify(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)