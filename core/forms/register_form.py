from fastapi.param_functions import Form


class RegisterForm:
    def __init__(
        self,
        email: str = Form(...),
        password: str = Form(...),
        retype_password: str = Form(...),
    ):
        self.email = email
        self.password = password
        self.retype_password = retype_password
        