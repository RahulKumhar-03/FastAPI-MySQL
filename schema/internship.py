from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean, String, CHAR, DateTime, Float
from database import Base
from datetime import datetime, date
import uuid
from pydantic import BaseModel

class Internship(Base):
    __tablename__ = 'internship'

    internshipId = Column(Integer, primary_key=True, index=True)
    degreeId = Column(Integer, ForeignKey('degree.degreeId'), nullable=False, unique=True)
    company = Column(String(100), nullable=False)
    jobPosition = Column(String(100), nullable=False)
    duration = Column(String(100), nullable=False)
    location = Column(String(100), nullable=False)
    supervisor = Column(String(50), nullable=False)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(String(50), nullable=True, default='admin')
    createdOn = Column(Date, default=datetime.now())
    changedBy = Column(String(50), nullable=True)
    changedOn = Column(Date, nullable=True)
    deletedBy = Column(String(50), nullable=True)
    deletedOn = Column(Date, nullable=True)

class InternshipBase(BaseModel):
    company: str
    jobPosition: str
    duration: str
    location: str
    supervisor: str

class InternshipCreate(InternshipBase):
    degreeId: int
    createdBy: str

class InternshipUpdate(InternshipBase):
    isActive: bool
    changedBy: str
    changedOn: datetime

class InternshipDelete(BaseModel):
    isActive: bool = False
    deletedBy: str
    deletedOn: datetime

class InternshipResponse(InternshipBase):
    internshipId: int