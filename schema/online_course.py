from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean, String, CHAR, DateTime, Float
from database import Base
from datetime import datetime, date
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
    createdBy = Column(String(50), nullable=True, default='admin')
    createdOn = Column(Date, default=datetime.now())
    changedBy = Column(String(50), nullable=True)
    changedOn = Column(Date, nullable=True)
    deletedBy = Column(String(50), nullable=True)
    deletedOn = Column(Date, nullable=True)

class OnlineCourseBase(BaseModel):
    platform: str
    course: str
    completionDate: datetime
    certificate: bool
    grade: str

class OnlineCourseCreate(OnlineCourseBase):
    educationId: int
    createdBy: str
    createdOn: date

class OnlineCourseUpdate(OnlineCourseBase):
    isActive: bool
    changedBy: str
    changedOn: date

class OnlineCourseResponse(OnlineCourseBase):
    onlineCourseId: int