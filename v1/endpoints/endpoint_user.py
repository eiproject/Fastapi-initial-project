from ..routes import *
from core import app, settings as APPSETTING
from core.forms.login_form import LoginForm
from core.forms.register_form import RegisterForm
from core.models.token import Token
from core.models.user import User
from datetime import timedelta
from db import get_db_session
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from v1.middleware_user import get_current_active_user
from v1.services.service_user import authenticate_user, create_access_token, create_new_user


@app.post(API_TOKEN, response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db_session)
    ):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=APPSETTING.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": f"{user.id}"}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post(API_LOGIN, response_model=Token)
async def login_for_access_token(
    form_data: LoginForm = Depends(), 
    db: Session = Depends(get_db_session)
    ):
    user = authenticate_user(db, form_data.email, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect email or password',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    access_token_expires = timedelta(minutes=APPSETTING.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'sub': f"{user.id}"}, 
        expires_delta=access_token_expires
    )
    return {
        'access_token': access_token, 
        'token_type': 'bearer'
        }


@app.post(API_REGISTER, response_model=User)
async def register_user(
    form_data: RegisterForm = Depends(), 
    db: Session = Depends(get_db_session)
    ):
    user = create_new_user(db, form_data)
    return {
        'email': user.email,
        'is_active': user.is_active
        }


@app.get(API_USER, response_model=User)
async def read_current_user(
    current_user: User = Depends(get_current_active_user)
    ):
    return {
        'email': current_user.email,
        'is_active': current_user.is_active
        }