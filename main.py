from datetime import datetime, timedelta
from typing import Annotated
from db.session import engine
from db.base import Base
from apis.base import api_router

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel


def include_router(app):   
	app.include_router(api_router)


def create_tables():         
	Base.metadata.create_all(bind=engine)
        

def start_application():
    app = FastAPI()
    create_tables()
    include_router(app)
    return app

app = start_application()

