from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from typing import List

from db.session import get_db
from db.models.conferences import Confernce
from schemas.conferences import ConferenceCreate,ShowConference
from db.repository.conferences import create_new_conference
from db.repository.conferences import create_new_conference,retreive_conference, retreive_conferences, update_conference_by_id, delete_conference_by_id
from db.models.user import User
from apis.v1.route_login import get_current_user_from_token, get_current_user_from_token_v2

router = APIRouter()


@router.post("/create-conference_v1/",response_model=ShowConference)
def create_conference(conference: ConferenceCreate,db: Session = Depends(get_db)):
    current_user = 1
    conference = create_new_conference(conference=conference,db=db,owner_id=current_user)
    return conference


@router.post("/create-conference_v2/",response_model=ShowConference)
def create_conference(conference: ConferenceCreate,db: Session = Depends(get_db),current_user:User = Depends(get_current_user_from_token)):
    #current_user = 1
    conference = create_new_conference(conference=conference,db=db,owner_id=current_user.id)
    return conference


@router.post("/create-conference_v2.1/",response_model=ShowConference)
def create_conference(conference: ConferenceCreate,db: Session = Depends(get_db),current_user:User = Depends(get_current_user_from_token_v2)):
    #current_user = 1
    conference = create_new_conference(conference=conference,db=db,owner_id=current_user.id)
    return conference


@router.get("/get_conference_byid/{id}",response_model=ShowConference) 
def read_conference(id:int,db:Session = Depends(get_db)):
    conference = retreive_conference(id=id,db=db)
    if not conference:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Conference with this id {id} does not exist")
    return conference


@router.get("/get_conferences/",response_model=List[ShowConference]) 
def read_conferences(db:Session = Depends(get_db)):
    conference = retreive_conferences(db=db)
    if not conference:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No Conference exists")
    return conference


@router.put("/update_conference_v1/{id}")
def update_confrence(id: int,conference: ConferenceCreate,db: Session = Depends(get_db)):
    current_user = 1
    message = update_conference_by_id(id=id,conference=conference,db=db,owner_id=current_user)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Conference with id {id} not found")
    return {"msg":"Successfully updated data."}


@router.put("/update_conference_v2/{id}")
def update_confrence(id: int,conference: ConferenceCreate,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    #current_user = 1
    conference_check = retreive_conference(id =id,db=db)
    if not conference_check:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Conference with {id} does not exist")
    print(conference_check.owner_id,current_user.id,current_user.is_superuser)
    if conference_check.owner_id == current_user.id or current_user.is_superuser:
        update_conference_by_id(id=id,conference=conference,db=db,owner_id=current_user.id)
        return {"msg":"Successfully updated data."}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"You are not permitted!!!!")



@router.put("/update_conference_v2.1/{id}")
def update_confrence(id: int,conference: ConferenceCreate,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token_v2)):
    #current_user = 1
    conference_check = retreive_conference(id =id,db=db)
    if not conference_check:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Conference with {id} does not exist")
    print(conference_check.owner_id,current_user.id,current_user.is_superuser)
    if conference_check.owner_id == current_user.id or current_user.is_superuser:
        update_conference_by_id(id=id,conference=conference,db=db,owner_id=current_user.id)
        return {"msg":"Successfully updated data."}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"You are not permitted!!!!")



@router.delete("/delete_conference_v1/{id}")
def delete_conference(id: int,db: Session = Depends(get_db)):
    current_user_id = 1
    message = delete_conference_by_id(id=id,db=db,owner_id=current_user_id)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Conference with id {id} not found")
    return {"msg":"Successfully deleted."}


@router.delete("/delete_conference_v2/{id}")
def delete_conferernce(id: int,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    conference = retreive_conference(id =id,db=db)
    if not conference:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Conference with {id} does not exist")
    print(conference.owner_id,current_user.id,current_user.is_superuser)
    if conference.owner_id == current_user.id or current_user.is_superuser:
        delete_conference_by_id(id=id,db=db,owner_id=current_user.id)
        return {"msg":"Successfully deleted."}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")



@router.delete("/delete_conference_v2.1/{id}")
def delete_conferernce(id: int,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token_v2)):
    conference = retreive_conference(id =id,db=db)
    if not conference:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Conference with {id} does not exist")
    print(conference.owner_id,current_user.id,current_user.is_superuser)
    if conference.owner_id == current_user.id or current_user.is_superuser:
        delete_conference_by_id(id=id,db=db,owner_id=current_user.id)
        return {"msg":"Successfully deleted."}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")

