from api import app
from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic_core import ValidationError


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    # Get the original 'detail' list of errors
    details = exc.errors()
    modified_details = []
    
    # Replace 'msg' with 'message' for each error
    for error in details:
        print(error)
        modified_details.append(f"{error["loc"][0]} is required.")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"message": modified_details}),
    )
