from sqlalchemy import Column, Integer, DateTime, ForeignKey, Boolean, CHAR, Float
from database import Base
from datetime import datetime
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
    createdBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    createdOn = Column(DateTime, default=datetime.now())
    changedBy = Column(Integer,ForeignKey('user.userId'), nullable=True)
    changedOn = Column(DateTime, nullable=True, onupdate=datetime.now())
    deletedBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    deletedOn = Column(DateTime, nullable=True)

class CourseBase(BaseModel):
    totalCredits: float 
    requiredCredits: float
    electiveCredits: float
    majorCredits: float
    minorCredits: float

class CourseCreate(CourseBase):
    degreeId: int

class CourseDelete(BaseModel):
    isActive: bool = False
    deletedOn: datetime = datetime.now()

class CourseResponse(CourseBase):
    courseId: int