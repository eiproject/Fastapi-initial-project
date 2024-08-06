from fastapi import Depends

from api.v1.repository.user_repository_impl import UserRepositoryImpl
from core.dto.login_dto import LoginDto
from core.model.token import Token
from core.service.user.login_user_service import LoginUserService

from ...path import PATH_LOGIN
from api import app
from api.v1.form.user.login_form import LoginForm
from psql_db import Session, get_db_session


@app.post(PATH_LOGIN, response_model=Token)
async def login_api(
    form_data: LoginForm = Depends(), 
    db: Session = Depends(get_db_session),
):
    dto = LoginDto(
        email=form_data.email,
        password=form_data.password,
    )
    service = LoginUserService(
        repository=UserRepositoryImpl(db)
    )
    token = service.execute(dto)
    return token