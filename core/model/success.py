from pydantic import BaseModel


class Success(BaseModel):
    is_success: bool
    