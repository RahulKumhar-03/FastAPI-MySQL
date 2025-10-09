from sqlalchemy import Column, Integer, ForeignKey, CHAR, Boolean, DateTime
from database import Base
import uuid
from datetime import datetime
from pydantic import BaseModel

class Education(Base):
    __tablename__ = 'education'

    educationId = Column(Integer, primary_key=True, index=True)
    personalInfoId = Column(Integer, ForeignKey('personalinfo.personalInfoId'), unique=True)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    createdOn = Column(DateTime, default=datetime.now())
    changedBy = Column(Integer,ForeignKey('user.userId'), nullable=True)
    changedOn = Column(DateTime, nullable=True, onupdate=datetime.now())
    deletedBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    deletedOn = Column(DateTime, nullable=True)

class EducationBase(BaseModel):
    personalInfoId: int

class EducationDelete(BaseModel):
    isActive: bool = False
    deletedOn: datetime = datetime.now()

class EducationResponse(EducationBase):
    educationId: int
