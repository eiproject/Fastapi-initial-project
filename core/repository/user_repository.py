from abc import ABC, abstractmethod

from core.model.user import UserInfo


class UserRepository(ABC):
    
    @abstractmethod
    def create(self, user: UserInfo) -> UserInfo:
        ...

    @abstractmethod
    def read(self, user: UserInfo) -> UserInfo:
        ...

    @abstractmethod
    def update(self) -> UserInfo:
        ...