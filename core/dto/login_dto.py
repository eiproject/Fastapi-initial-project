from pydantic import BaseModel


class LoginDto(BaseModel):
    email: str | None
    password: str | None
    