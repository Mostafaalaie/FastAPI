from sqlalchemy.orm import Session

from schemas.conferences import ConferenceCreate
from db.models.conferences import Confernce


def create_new_conference(conference: ConferenceCreate,db: Session,owner_id:int):
    conference_object = Confernce(**conference.dict(),owner_id=owner_id)
    db.add(conference_object)
    db.commit()
    db.refresh(conference_object)
    return conference_object

def retreive_conference(id:int,db:Session):
    item = db.query(Confernce).filter(Confernce.id == id).first()
    return item

def retreive_conferences(db:Session):
    conferences =  db.query(Confernce).all()
    return conferences

def update_conference_by_id(id:int, conference: ConferenceCreate,db: Session,owner_id):
    existing_conference = db.query(Confernce).filter(Confernce.id == id)
    if not existing_conference.first():
        return 0
    conference.__dict__.update(owner_id=owner_id)  
    existing_conference.update(conference.__dict__)
    db.commit()
    return 1

def delete_conference_by_id(id: int,db: Session,owner_id):
    existing_conference = db.query(Confernce).filter(Confernce.id == id)
    if not existing_conference.first():
        return 0
    existing_conference.delete(synchronize_session=False)
    db.commit()
    return 1