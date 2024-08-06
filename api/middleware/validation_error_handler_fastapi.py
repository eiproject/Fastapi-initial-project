from api import app
from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


@app.exception_handler(RequestValidationError)
async def standard_validation_exception_handler(request: Request, exc: RequestValidationError):
    # Get the original 'detail' list of errors
    details = exc.errors()
    modified_details = []
    
    # Replace 'msg' with 'message' for each error
    for error in details:
        error_location = error["loc"][1] if len(error["loc"]) > 1 else error["loc"][0]
        modified_details.append(f"{error_location} is required.")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"message": modified_details}),
    )