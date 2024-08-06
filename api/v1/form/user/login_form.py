from dataclasses import dataclass
from fastapi.param_functions import Form

@dataclass
class LoginForm:
    email: str = Form(...)
    password: str = Form(...)
