from datetime import timedelta
from fastapi import Depends, HTTPException, status
from core.models.token import Token
from core.models.user import User
from core.models.database import fake_users_db
from v1.endpoints.middleware_user import get_current_active_user
from fastapi.security import OAuth2PasswordRequestForm
from v1.endpoints.services_user import authenticate_user, create_access_token
from . import app, APP_SETTINGS

@app.get("/")
async def hello_world():
    return {"message": "Hello World"}


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=APP_SETTINGS.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]