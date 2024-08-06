from pydantic import BaseModel
from datetime import datetime

from core.dto.login_dto import LoginDto
from core.dto.register_dto import RegisterDto
from core.utils.password import generate_hash
from core.utils.time import get_now


class User(BaseModel):
    user_id: int
    email: str

    @staticmethod
    def new_from_dict(data: dict):
        return User(
            user_id=data.get('user_id'),
            email=data.get('email'),
        )

class UserInfo(User):
    password_hash: str
    date_created: datetime | None
    date_updated: datetime | None
    
    @staticmethod
    def new_from_register(dto: RegisterDto):
        if dto.password != dto.retype_password:
            raise ValueError('Password and retyped password not match')
        
        return UserInfo(
            user_id=-1,
            email=dto.email,
            password_hash=generate_hash(dto.password),
            date_created=get_now(),
            date_updated=None,
        )
    
    @staticmethod
    def new_from_login(dto: LoginDto):
        return UserInfo(
            user_id=-1,
            email=dto.email,
            password_hash=generate_hash(dto.password),
            date_created=None,
            date_updated=None,
        )
    
    @staticmethod
    def new_from_dict(data: dict):
        return UserInfo(
            user_id=data.get('user_id'),
            email=data.get('email'),
            password_hash=data.get('password_hash'),
            date_created=data.get('created_date'),
            date_updated=data.get('updated_date'),
        )
        
    def asUser(self) -> User:
        return User(
            user_id=self.user_id, 
            email=self.email
        )
        