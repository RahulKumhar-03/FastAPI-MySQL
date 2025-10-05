from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean, String, CHAR, DateTime, Float
from database import Base
from datetime import datetime, date
import uuid
from pydantic import BaseModel

class ActivityMapping(Base):
    __tablename__ = 'activitymapping'

    activityMappingId = Column(Integer, primary_key=True, index=True)
    activityId = Column(Integer, ForeignKey('activity.activityId'), nullable=False)
    degreeId = Column(Integer, ForeignKey('degree.degreeId'), nullable=False)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(String(50), nullable=True, default='admin')
    createdOn = Column(Date, default=datetime.now())
    changedBy = Column(String(50), nullable=True)
    changedOn = Column(Date, nullable=True)
    deletedBy = Column(String(50), nullable=True)
    deletedOn = Column(Date, nullable=True)

class ActivityMappingBase(BaseModel):
    activityId: int
    degreeId: int

class ActivityMappingCreate(ActivityMappingBase):
    createdBy: str
    createdOn: date

class ActivityMappingUpdate(ActivityMappingBase):
    isActive: bool
    changedBy: str
    changedOn: date