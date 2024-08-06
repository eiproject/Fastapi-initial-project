from api import app
from api.exception import AuthException
from fastapi import status
from fastapi.responses import JSONResponse


@app.exception_handler(AuthException)
async def auth_exception_handler(request, exc: AuthException):
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={
        "message": str(exc),
    })
