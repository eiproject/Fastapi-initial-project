from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .settings import SQLALCHEMY_DATABASE_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    echo=True,
    connect_args={}
    )

SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
    )

def get_db_session() -> sessionmaker: # type: ignore
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
