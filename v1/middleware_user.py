from core import oauth2_scheme, settings as APPSETTING
from core.models.token_data import TokenData
from db import get_db_session
from db.contexts.context_user import get_user
from db.models import UserDto
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from sqlalchemy.orm import Session


def get_current_user(
    token: str = Depends(oauth2_scheme), 
    db: Session = Depends(get_db_session)
    ):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, 
            APPSETTING.SECRET_KEY, 
            algorithms=[APPSETTING.ALGORITHM]
            )
        
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        token_data = TokenData(user_id=user_id)
    except JWTError as e:
        raise credentials_exception
    user = get_user(db, user_id=token_data.user_id)
    if user is None:
        raise credentials_exception
    return user


def get_current_active_user(current_user: UserDto = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user