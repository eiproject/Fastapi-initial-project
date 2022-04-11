from core.models.user import UserCredential
from db import models
from sqlalchemy.orm import Session
from typing import List, Optional


def get_user(db: Session, user_id: int) -> Optional[models.UserDto]:
    return db.query(models.UserDto).filter(models.UserDto.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> Optional[models.UserDto]:
    return db.query(models.UserDto).filter(models.UserDto.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[models.UserDto]:
    return db.query(models.UserDto).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCredential) -> models.UserDto:
    new_user = models.UserDto(
        email=user.email, 
        hashed_password=user.hashed_password
        )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
