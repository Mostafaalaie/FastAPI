from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from typing import List

from schemas.user import UserCreate, ShowUser
from db.session import get_db
from db.repository.user import create_new_user, retreive_users

router = APIRouter()


@router.post("/create_user", response_model= ShowUser)
def create_user(user : UserCreate,db: Session = Depends(get_db)):
    user = create_new_user(user=user,db=db)
    return user

@router.get("/get_users/",response_model=List[ShowUser]) 
def read_users(db:Session = Depends(get_db)):
    users = retreive_users(db=db)
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No User exists")
    return users

