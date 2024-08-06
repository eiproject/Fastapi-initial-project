import os

from datetime import timedelta
from jose import jwt

from core.model.token import Token
from core.model.user import User
from core.utils.time import get_now


def create_access_token(user: User) -> Token:
    to_encode = user.model_dump()
    expire = get_now() + timedelta(hours=int(os.getenv('ACCESS_TOKEN_EXPIRE_HOURS')))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv('SECRET_KEY'), algorithm=os.getenv('ALGORITHM'))
    return Token(access_token=encoded_jwt)

def decode_access_token(token: Token) -> User:
    # will raise JWTError when err
    payload = jwt.decode(token.access_token, os.getenv('SECRET_KEY'), algorithms=os.getenv('ALGORITHM'))
    return User.new_from_dict(payload)
