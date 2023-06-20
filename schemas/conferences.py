from typing import Optional
from pydantic import BaseModel
from datetime import date,datetime


#shared properties
class ConferenceBase(BaseModel):
    title : Optional[str] = None
    description : Optional[str] = None
    start_time : Optional[date] = datetime.now().date()
    end_time : Optional[date] = datetime.now().date()
    

#this will be used to validate data while creating a Conference
class ConferenceCreate(ConferenceBase):
    title : str 
    
#this will be used to format the response to not to have id,owner_id etc
class ShowConference(ConferenceBase):
    id : int
    title : str
    start_time : date
    description : Optional[str]
    capasity : int

    class Config():  #to convert non dict obj to json
        orm_mode = True