from ...path import PATH_TEST_PUBLIC_API, PATH_TEST_PRIVATE_API
from api import app
from api.injection.authorization import get_current_user
from core.model.success import Success
from core.model.user import User
from fastapi import Depends
from psql_db import Session, get_db_session


@app.get(PATH_TEST_PRIVATE_API, response_model=Success)
async def private_api(
    db: Session = Depends(get_db_session),
    user: User = Depends(get_current_user),
):
    return Success(is_success=True)

@app.get(PATH_TEST_PUBLIC_API, response_model=Success)
async def public_api(
    db: Session = Depends(get_db_session),
):
    return Success(is_success=True)
