from datetime import datetime
from sqlalchemy.orm import Mapped
from sqlalchemy import Column, Integer, String, DateTime
from .base import Base

class UserModel(Base):
    __tablename__ = "users"

    user_id: Mapped[str] = Column(Integer, primary_key=True, index=True)
    email: Mapped[str] = Column(String, unique=True, nullable=False)
    password_hash: Mapped[str] = Column(String, nullable=False)
    date_created: Mapped[datetime] = Column(DateTime, nullable=False)
    date_updated: Mapped[datetime] = Column(DateTime)