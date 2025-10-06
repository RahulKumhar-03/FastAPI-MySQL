from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean, String, CHAR, DateTime, Float
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
    createdBy = Column(String(50), nullable=True, default='admin')
    createdOn = Column(Date, default=datetime.now())
    changedBy = Column(String(50), nullable=True)
    changedOn = Column(Date, nullable=True)
    deletedBy = Column(String(50), nullable=True)
    deletedOn = Column(Date, nullable=True)

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
    createdBy: str
    createdOn: date

class DegreeUpdate(DegreeBase):
    isActive: bool
    changedBy: str
    changedOn: date

class DegreeDelete(BaseModel):
    isActive: bool = False
    deletedBy: str
    deletedOn: datetime

class DegreeResponse(DegreeBase):
    degreeId : int