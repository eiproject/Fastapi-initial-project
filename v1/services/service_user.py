from core import pwd_context, settings as APP_SETTINGS
from core.forms.register_form import RegisterForm
from core.models.user import UserCredential
from datetime import datetime, timedelta
from db.contexts.context_user import get_user, get_user_by_email, create_user
from db.models import UserDto
from fastapi import HTTPException
from jose import JWTError, jwt
from typing import Optional


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_new_user(db, register_form: RegisterForm) -> UserDto:
    user = get_user_by_email(db, register_form.email)
    
    if user is None and (register_form.password == register_form.retype_password):
        credential  = UserCredential(
            email=register_form.email,
            hashed_password=get_password_hash(register_form.password)
        )
        user = create_user(db, credential)
        
    elif user is not None:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    else:
        raise HTTPException(status_code=400, detail="Password not match")
    
    return user 


def authenticate_user(db, email: str, password: str) -> Optional[UserDto]:
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, 
        APP_SETTINGS.SECRET_KEY, 
        algorithm=APP_SETTINGS.ALGORITHM
        )

    return encoded_jwt