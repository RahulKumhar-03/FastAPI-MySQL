from sqlalchemy import Column, Integer, Date, Boolean, String, CHAR
from database import Base
from datetime import datetime
import uuid
from pydantic import BaseModel

class Activity(Base):
    __tablename__ = 'activity'

    activityId = Column(Integer, primary_key=True, index=True)
    activityName = Column(String(100), nullable=False)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(String(50), nullable=True, default='admin')
    createdOn = Column(Date, default=datetime.now())
    changedBy = Column(String(50), nullable=True)
    changedOn = Column(Date, nullable=True)
    deletedBy = Column(String(50), nullable=True)
    deletedOn = Column(Date, nullable=True)

class ActivityBase(BaseModel):
    activityName: str
    isActive: bool

class ActivityCreate(ActivityBase):
    createdBy: str
    createdOn: datetime

class ActivityUpdate(ActivityBase):
    changedBy: str
    changedOn: datetime

class ActivityDelete(BaseModel):
    isActive: bool = False
    deletedBy: str
    deletedOn: datetime

class ActivityResponse(ActivityBase):
    activityId: int