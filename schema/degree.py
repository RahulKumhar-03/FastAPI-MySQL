from sqlalchemy import Column, Integer, ForeignKey, Boolean, String, CHAR, DateTime, Float
from database import Base
from datetime import datetime, date
import uuid
from pydantic import BaseModel

class Degree(Base):
    __tablename__ = 'degree'

    degreeId = Column(Integer, primary_key=True, index=True)
    educationId = Column(Integer, ForeignKey('education.educationId'), nullable=False)
    institution = Column(String(100), nullable=False)
    major = Column(String(200), nullable=False)
    minor = Column(String(100), nullable=False)
    startDate = Column(DateTime, nullable=False)
    endDate = Column(DateTime, nullable=False)
    gpa = Column(Float, nullable=False)
    credits = Column(Float, nullable=False)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    createdOn = Column(DateTime, default=datetime.now())
    changedBy = Column(Integer,ForeignKey('user.userId'), nullable=True)
    changedOn = Column(DateTime, nullable=True, onupdate=datetime.now())
    deletedBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    deletedOn = Column(DateTime, nullable=True)

class DegreeBase(BaseModel):
    institution: str
    major: str
    minor: str
    startDate: date
    endDate: date
    gpa: float
    credits: float

class DegreeCreate(DegreeBase):
    educationId: int

class DegreeDelete(BaseModel):
    isActive: bool = False
    deletedOn: datetime = datetime.now()

class DegreeResponse(DegreeBase):
    degreeId : int