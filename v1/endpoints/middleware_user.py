from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from . import APP_SETTINGS, oauth2_scheme
from .services_user import get_user
from core.models.token_data import TokenData
from core.models.user import User
from core.models.database import fake_users_db

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, 
            APP_SETTINGS.SECRET_KEY, 
            algorithms=[APP_SETTINGS.ALGORITHM]
            )
        
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user