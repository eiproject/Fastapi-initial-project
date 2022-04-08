from . import Base
from sqlalchemy import Boolean, Column, Integer, String

class UserDto(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

# to create table automatically
# sqlalchemy does not support alter
# Base.metadata.create_all()