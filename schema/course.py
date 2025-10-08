from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean, String, CHAR, DateTime, Float
from database import Base
from datetime import datetime, date
import uuid
from pydantic import BaseModel

class Course(Base):
    __tablename__ = 'course'

    courseId = Column(Integer, primary_key=True, index=True)
    degreeId = Column(Integer, ForeignKey('degree.degreeId'), nullable=False, unique=True)
    totalCredits = Column(Float, nullable=False)
    requiredCredits = Column(Float, nullable=False)
    electiveCredits = Column(Float, nullable=False)
    majorCredits = Column(Float, nullable=False)
    minorCredits = Column(Float, nullable=False)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(String(50), nullable=True, default='admin')
    createdOn = Column(Date, default=datetime.now())
    changedBy = Column(String(50), nullable=True)
    changedOn = Column(Date, nullable=True)
    deletedBy = Column(String(50), nullable=True)
    deletedOn = Column(Date, nullable=True)

class CourseBase(BaseModel):
    totalCredits: float 
    requiredCredits: float
    electiveCredits: float
    majorCredits: float
    minorCredits: float

class CourseCreate(CourseBase):
    degreeId: int
    createdBy: str

class CourseUpdate(CourseBase):
    isActive: bool
    changedBy: str
    changedOn: datetime

class CourseDelete(BaseModel):
    isActive: bool = False
    deletedBy: str
    deletedOn: datetime

class CourseResponse(CourseBase):
    courseId: int