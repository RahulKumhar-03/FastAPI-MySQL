from sqlalchemy import Column, Integer, DateTime, ForeignKey, Boolean, String, CHAR
from database import Base
from datetime import datetime
import uuid
from pydantic import BaseModel

class Project(Base):
    __tablename__ = 'project'

    projectId = Column(Integer, primary_key=True, index=True)
    internshipId = Column(Integer, ForeignKey('internship.internshipId'), nullable=False)
    projectName = Column(String(100), nullable=False)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    createdOn = Column(DateTime, default=datetime.now())
    changedBy = Column(Integer,ForeignKey('user.userId'), nullable=True)
    changedOn = Column(DateTime, nullable=True, onupdate=datetime.now())
    deletedBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    deletedOn = Column(DateTime, nullable=True)

class ProjectBase(BaseModel):
    projectName: str

class ProjectCreate(ProjectBase):
    internshipId: int

class ProjectDelete(BaseModel):
    isActive: bool = False
    deletedOn: datetime = datetime.now()

class ProjectResponse(ProjectBase):
    projectId: int