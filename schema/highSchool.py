from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean, String, CHAR, DateTime, Float
from database import Base
from datetime import datetime, date
import uuid
from pydantic import BaseModel

class HighSchool(Base):
    __tablename__ = 'highschool'

    highSchoolId = Column(Integer, primary_key=True, index=True)
    educationId = Column(Integer, ForeignKey('education.educationId'), nullable=False)
    highSchoolName = Column(String(100), nullable=False)
    graduationYear = Column(DateTime, nullable=False)
    gpa = Column(Float, nullable=False)
    valedictorian = Column(Boolean, nullable=False)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(String(50), nullable=True, default='admin')
    createdOn = Column(Date, default=datetime.now())
    changedBy = Column(String(50), nullable=True)
    changedOn = Column(Date, nullable=True)
    deletedBy = Column(String(50), nullable=True)
    deletedOn = Column(Date, nullable=True)

class HighSchoolBase(BaseModel):
    highSchoolName: str
    graduationYear: date
    gpa: float
    valedictorian: bool

class HighSchoolCreate(HighSchoolBase):
    educationId: int
    createdBy: str
    createdOn: date

class HighSchoolUpdate(HighSchoolBase):
    isActive: bool
    changedBy: str
    changedOn: date

class HighSchoolResponse(HighSchoolBase):
    highSchoolId: int