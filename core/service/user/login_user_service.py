from api.exception import AuthException
from core.dto.login_dto import LoginDto
from core.model.user import UserInfo
from core.model.token import Token
from core.repository.user_repository import UserRepository
from core.static.custom_message import INCORRECT_EMAIL_OR_PASSWORD
from core.utils.password import verify_password
from core.utils.token import create_access_token, decode_access_token


class LoginUserService:
    repository: UserRepository
    
    def __init__(self, repository: UserRepository):
        self.repository = repository
        
    def execute(self, login_dto: LoginDto) -> Token:
        user = UserInfo.new_from_login(login_dto)
        user = self.repository.read(user)
        
        if not verify_password(
            plain_password=login_dto.password,
            hashed_password=user.password_hash,
        ):
            raise AuthException(INCORRECT_EMAIL_OR_PASSWORD)
        
        user_safe_dict = user.asUser()
        token = create_access_token(user_safe_dict)
        return token
    