# jwt token and verify token
from jose import JWTError, jwt
# import datetime and timedelta
from datetime import datetime, timedelta
from . import schemas

# import fastapi and status and HTTPException
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer


# create oauth2_scheme
# login url is able to get token only
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# SECRET_KEY and ALGORITHM and ACCESS_TOKEN_EXPIRE_MINUTES
# SECRET_KEY is a random string and ALGORITHM is HS256
SECRET_KEY = "123456789ABCDEFG"
ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES is 30 minutes
ACCESS_TOKEN_EXPIRE_MINUTES = 30





# create function to create an access token
# create_access_token function takes data as argument
# data is a dictionary
# to_encode is a copy of data
# expire is a datetime object
# to_encode is updated with exp key
# encoded_jwt is a jwt token
# return encoded_jwt
def create_access_token(data: dict):
    # update data with exp key
    to_encode = data.copy()

    # adding expire key to to_encode
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    # encode to_encode with SECRET_KEY and ALGORITHM
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# create function to verify access token
# verify_access_token function takes token and credentials_exceptions as argument
# credentials_exceptions is a HTTPException object
# payload is a dictionary
# id is a string
# token_data is a TokenData object
def verify_access_token(token: str, credentials_exceptions):
    # tries to decode token or else raise credentials_exceptions
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        # get id from payload
        id: str = payload.get("user_id")
        if id is None:
            return credentials_exceptions
        token_data = schemas.TokenData(id=id)
    
    # checks if token is expired or else raise credentials_exceptions
    except JWTError:
        raise credentials_exceptions
    return token_data



# get user from token
# only users are able to get access to posts
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentails_exceptions = HTTPException(
        status_code=401,
        detail=f"Could not validate credentials",
        headers={
            "WWW-Authenticate": "Bearer"
        }
    )
    # only gives access to users
    return verify_access_token(token, credentails_exceptions)
