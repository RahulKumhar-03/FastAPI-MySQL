from sqlalchemy import Column, Integer, ForeignKey, Boolean, String, CHAR, DateTime, Float
from database import Base
from datetime import datetime
import uuid
from pydantic import BaseModel

class CompletedCourse(Base):
    __tablename__ = 'completedcourse'

    completedCourseId = Column(Integer, primary_key=True, index=True)
    courseId = Column(Integer, ForeignKey('course.courseId'), nullable=False, unique=True)
    courseCode = Column(String(100), nullable=False)
    completedCourseName = Column(String(100), nullable=False)
    credits = Column(Float, nullable=False)
    grade = Column(String(50), nullable=False)
    semester = Column(String(50), nullable=False)
    professor = Column(String(100), nullable=False)
    courseDescription = Column(String(200), nullable=False)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    createdOn = Column(DateTime, default=datetime.now())
    changedBy = Column(Integer,ForeignKey('user.userId'), nullable=True)
    changedOn = Column(DateTime, nullable=True, onupdate=datetime.now())
    deletedBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    deletedOn = Column(DateTime, nullable=True)
    
class CompletedCourseBase(BaseModel):
    courseCode: str
    completedCourseName: str
    credits: float
    grade: str
    semester: str
    professor: str
    courseDescription: str

class CompletedCourseCreate(CompletedCourseBase):
    courseId: int

class CompletedCourseDelete(BaseModel):
    isActive: bool = False
    deletedOn: datetime = datetime.now()

class CompletedCourseResponse(CompletedCourseBase):
    completedCourseId: int