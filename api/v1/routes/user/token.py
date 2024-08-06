from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from api.v1.repository.user_repository_impl import UserRepositoryImpl
from core.dto.login_dto import LoginDto
from core.model.token import Token
from core.service.user.login_user_service import LoginUserService

from ...path import PATH_TOKEN
from api import app
from psql_db import Session, get_db_session


@app.post(PATH_TOKEN, response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db_session),
    ):
    dto = LoginDto(
        email=form_data.username,
        password=form_data.password,
    )
    service = LoginUserService(
        repository=UserRepositoryImpl(db)
    )
    token = service.execute(dto)
    return token
