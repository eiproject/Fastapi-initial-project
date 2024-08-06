from core.dto.register_dto import RegisterDto
from core.model.token import Token
from core.model.user import UserInfo
from core.repository.user_repository import UserRepository
from core.utils.token import create_access_token


class RegisterUserService:
    repository: UserRepository
    
    def __init__(self, repository: UserRepository):
        self.repository = repository
        
    def execute(self, regiser_dto: RegisterDto) -> Token:
        user = UserInfo.new_from_register(regiser_dto)
        user = self.repository.create(user)
        
        user_safe_dict = user.asUser()
        token = create_access_token(user_safe_dict)
        return token
    