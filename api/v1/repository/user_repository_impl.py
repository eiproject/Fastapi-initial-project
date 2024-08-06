from api.exception import AuthException
from core.static.custom_message import EMAIL_ALREADY_REGISTERED, USER_DOESNT_EXISTS
from core.model.user import UserInfo
from core.repository.user_repository import UserRepository
from psql_db import Session
from psql_db.model.user_model import UserModel


class UserRepositoryImpl(UserRepository):
    
    def __init__(self, db: Session) -> None:
        super().__init__()
        self.db = db
        
    def create(self, user: UserInfo) -> UserInfo:
        if self._select_user_by_email(user.email):
            raise ValueError(EMAIL_ALREADY_REGISTERED)
        
        model = UserModel(
            email=user.email,
            password_hash=user.password_hash,
            date_created=user.date_created,
            date_updated=user.date_updated,
        )
        
        self.db.add(model)
        self.db.commit()
        return UserInfo.new_from_dict(model.to_dict())
        
        
    def read(self, user: UserInfo) -> UserInfo:
        if user.user_id is not None and user.user_id >= 0:
            model = self._select_user_by_id(user_id=user.user_id)
            if model: 
                return UserInfo.new_from_dict(model.to_dict())
            
        if user.email is not None:
            model = self._select_user_by_email(user.email)
            if model: 
                return UserInfo.new_from_dict(model.to_dict())
        
        raise AuthException(USER_DOESNT_EXISTS)

    def update(self) -> UserInfo:
        ...
        
    def _select_user_by_id(self, user_id: int) -> UserModel:
        return self.db.query(UserModel).filter(UserModel.user_id == user_id).one_or_none()
    
    def _select_user_by_email(self, email: str) -> UserModel:
        return self.db.query(UserModel).filter(UserModel.email.ilike(email)).one_or_none()
