from api import app
from fastapi import status
from fastapi.responses import JSONResponse


@app.exception_handler(ValueError)
async def value_error_request_handler(request, exc: ValueError):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={
        "message": str(exc),
    })
