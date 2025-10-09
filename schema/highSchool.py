from sqlalchemy import Column, Integer, ForeignKey, Boolean, String, CHAR, DateTime, Float
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
    createdBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    createdOn = Column(DateTime, default=datetime.now())
    changedBy = Column(Integer,ForeignKey('user.userId'), nullable=True)
    changedOn = Column(DateTime, nullable=True, onupdate=datetime.now())
    deletedBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    deletedOn = Column(DateTime, nullable=True)

class HighSchoolBase(BaseModel):
    highSchoolName: str
    graduationYear: date
    gpa: float
    valedictorian: bool

class HighSchoolCreate(HighSchoolBase):
    educationId: int

class HighSchoolDelete(BaseModel):
    isActive: bool = False
    deletedOn: datetime = datetime.now()

class HighSchoolResponse(HighSchoolBase):
    highSchoolId: int