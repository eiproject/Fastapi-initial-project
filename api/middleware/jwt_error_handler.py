from api import app
from fastapi import status
from fastapi.responses import JSONResponse
from jose import JWTError


@app.exception_handler(JWTError)
async def value_error_handler(request, exc: JWTError):
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={
        "message": "Unauthorized.",
    })
