from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .settings import *

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={}
    )

SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
    )

Base = declarative_base(engine)

def get_db_session() -> sessionmaker:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
