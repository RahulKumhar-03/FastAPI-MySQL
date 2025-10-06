from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean, String, CHAR
from database import Base
from datetime import datetime, date
import uuid
from pydantic import BaseModel

class Project(Base):
    __tablename__ = 'project'

    projectId = Column(Integer, primary_key=True, index=True)
    internshipId = Column(Integer, ForeignKey('internship.internshipId'), nullable=False)
    projectName = Column(String(100), nullable=False)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(String(50), nullable=True, default='admin')
    createdOn = Column(Date, default=datetime.now())
    changedBy = Column(String(50), nullable=True)
    changedOn = Column(Date, nullable=True)
    deletedBy = Column(String(50), nullable=True)
    deletedOn = Column(Date, nullable=True)

class ProjectBase(BaseModel):
    projectName: str

class ProjectCreate(ProjectBase):
    internshipId: int
    createdBy: str
    createdOn: date

class ProjectUpdate(ProjectBase):
    isActive: bool
    changedBy: str
    changedOn: date

class ProjectResponse(ProjectBase):
    projectId: int