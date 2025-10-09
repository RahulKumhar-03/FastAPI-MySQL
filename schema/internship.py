from sqlalchemy import Column, Integer, ForeignKey, Boolean, String, CHAR, DateTime
from database import Base
from datetime import datetime
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
    createdBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    createdOn = Column(DateTime, default=datetime.now())
    changedBy = Column(Integer,ForeignKey('user.userId'), nullable=True)
    changedOn = Column(DateTime, nullable=True, onupdate=datetime.now())
    deletedBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    deletedOn = Column(DateTime, nullable=True)

class InternshipBase(BaseModel):
    company: str
    jobPosition: str
    duration: str
    location: str
    supervisor: str

class InternshipCreate(InternshipBase):
    degreeId: int

class InternshipDelete(BaseModel):
    isActive: bool = False
    deletedOn: datetime = datetime.now()

class InternshipResponse(InternshipBase):
    internshipId: int