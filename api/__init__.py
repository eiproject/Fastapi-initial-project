import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from api.v1.path import PATH_TOKEN
# from .routes import API_TOKEN


root_path = os.getenv('FASTAPI_ROOT_PATH', default='').strip()
app = FastAPI(
    root_path=root_path,
)

pwd_context = CryptContext(
    schemes=["bcrypt"], 
    deprecated="auto"
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=PATH_TOKEN
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# from .settings import *
from .routes import *
from .middleware import *