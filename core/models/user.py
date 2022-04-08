from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    email: Optional[str] = None
    is_active: Optional[bool] = None
    
    
class UserCredential(User):
    hashed_password: str