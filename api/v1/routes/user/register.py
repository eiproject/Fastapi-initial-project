from fastapi import Depends

from api.v1.repository.user_repository_impl import UserRepositoryImpl
from core.dto.register_dto import RegisterDto
from core.model.token import Token
from core.service.user.register_user_service import RegisterUserService

from ...path import PATH_REGISTER
from api import app
from api.v1.form.user.register_form import RegisterForm
from psql_db import Session, get_db_session


@app.post(PATH_REGISTER, response_model=Token)
async def register_api(
    form_data: RegisterForm = Depends(), 
    db: Session = Depends(get_db_session),
):
    dto = RegisterDto(
        email=form_data.email,
        password=form_data.password,
        retype_password=form_data.retype_password,
    )
    service = RegisterUserService(
        repository=UserRepositoryImpl(db)
    )
    token = service.execute(dto)
    return token