from sqlalchemy import Column, Integer, ForeignKey, Boolean, String, CHAR, DateTime
from database import Base
from datetime import datetime 
import uuid
from pydantic import BaseModel

class OnlineCourse(Base):
    __tablename__ = 'onlinecourse'

    onlineCourseId = Column(Integer, primary_key=True, index=True)
    educationId = Column(Integer, ForeignKey('education.educationId'), nullable=False)
    platform = Column(String(100), nullable=False)
    course = Column(String(100), nullable=False)
    completionDate = Column(DateTime, nullable=False)
    certificate = Column(Boolean, nullable=False, default=True)
    grade = Column(String(30), nullable=False)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    createdOn = Column(DateTime, default=datetime.now())
    changedBy = Column(Integer,ForeignKey('user.userId'), nullable=True)
    changedOn = Column(DateTime, nullable=True, onupdate=datetime.now())
    deletedBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    deletedOn = Column(DateTime, nullable=True)

class OnlineCourseBase(BaseModel):
    platform: str
    course: str
    completionDate: datetime
    certificate: bool
    grade: str

class OnlineCourseCreate(OnlineCourseBase):
    educationId: int

class OnlineCourseDelete(BaseModel):
    isActive: bool = False
    deletedOn: datetime = datetime.now()

class OnlineCourseResponse(OnlineCourseBase):
    onlineCourseId: int