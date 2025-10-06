from sqlalchemy import Column, Integer, ForeignKey, CHAR, Boolean, String, Date
from database import Base
import uuid
from datetime import datetime, date
from pydantic import BaseModel

class Education(Base):
    __tablename__ = 'education'

    educationId = Column(Integer, primary_key=True, index=True)
    personalInfoId = Column(Integer, ForeignKey('personalinfo.personalInfoId'), unique=True)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(String(50), nullable=True, default='admin')
    createdOn = Column(Date, default=datetime.now())
    changedBy = Column(String(50), nullable=True)
    changedOn = Column(Date, nullable=True)
    deletedBy = Column(String(50), nullable=True)
    deletedOn = Column(Date, nullable=True)

class EducationBase(BaseModel):
    personalInfoId: int

class EducationCreate(EducationBase):
    createdBy: str
    createdOn: date

class EducationDelete(BaseModel):
    isActive: bool = False
    deletedBy: str
    deletedOn: datetime

class EducationResponse(EducationBase):
    educationId: int
