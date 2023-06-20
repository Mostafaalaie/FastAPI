from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Confernce(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    start_time = Column(DateTime, default=datetime.now)
    end_time = Column(DateTime, default=datetime.now)
    capasity = Column(Integer, default=0)
    owner_id =  Column(Integer,ForeignKey("user.id"))
    owner = relationship("User")
