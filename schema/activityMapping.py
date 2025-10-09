from sqlalchemy import Column, Integer, DateTime, ForeignKey, Boolean, CHAR
from database import Base
from datetime import datetime
import uuid
from pydantic import BaseModel

class ActivityMapping(Base):
    __tablename__ = 'activitymapping'

    activityMappingId = Column(Integer, primary_key=True, index=True)
    activityId = Column(Integer, ForeignKey('activity.activityId'), nullable=False)
    degreeId = Column(Integer, ForeignKey('degree.degreeId'), nullable=False)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    createdOn = Column(DateTime, default=datetime.now())
    changedBy = Column(Integer,ForeignKey('user.userId'), nullable=True)
    changedOn = Column(DateTime, nullable=True, onupdate=datetime.now())
    deletedBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    deletedOn = Column(DateTime, nullable=True)

class ActivityMappingBase(BaseModel):
    activityId: int
    degreeId: int

class ActivityMappingDelete(BaseModel):
    isActive: bool = False
    deletedOn: datetime = datetime.now()

class ActivityMappingResponse(ActivityMappingBase):
    activityMappingId: int