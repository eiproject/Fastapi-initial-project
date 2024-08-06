from dataclasses import dataclass
from fastapi.param_functions import Form

@dataclass
class RegisterForm:
    email: str = Form(...)
    password: str = Form(...)
    retype_password: str = Form(...)
    