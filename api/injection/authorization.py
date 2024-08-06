from api import oauth2_scheme
from core.model.token import Token
from core.utils.token import decode_access_token
from fastapi import Depends, HTTPException, status
from jose import JWTError


def get_current_user(
    request_token: str = Depends(oauth2_scheme), 
    ):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        if "Bearer" in request_token or "bearer" in request_token:
            request_token = request_token.split(' ')[-1]
        
        token_obj = Token(access_token=request_token)
        user = decode_access_token(token=token_obj)
        return user
    except JWTError as e:
        raise credentials_exception
    