from pydantic import BaseModel


class RegisterDto(BaseModel):
    email: str | None = None
    password: str | None = None
    retype_password: str | None = None
    