from sqlalchemy import Column, Integer, DateTime, ForeignKey, Boolean, String, CHAR, Float
from database import Base
from datetime import datetime
import uuid
from pydantic import BaseModel

class Thesis(Base):
    __tablename__ = 'thesis'

    thesisId = Column(Integer, primary_key=True, index=True)
    degreeId = Column(Integer, ForeignKey('degree.degreeId'), nullable=False, unique=True)
    title = Column(String(100), nullable=False)
    advisor = Column(String(100), nullable=False)
    grade = Column(String(100), nullable=False)
    published = Column(Boolean, nullable=False, default=True)
    citations = Column(Float, nullable=False)
    abstract = Column(String(100), nullable=False)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    createdOn = Column(DateTime, default=datetime.now())
    changedBy = Column(Integer,ForeignKey('user.userId'), nullable=True)
    changedOn = Column(DateTime, nullable=True, onupdate=datetime.now())
    deletedBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    deletedOn = Column(DateTime, nullable=True)

class ThesisBase(BaseModel):
    title: str 
    advisor: str
    grade: str
    published: bool
    citations: float
    abstract: str

class ThesisCreate(ThesisBase):
    degreeId: int

class ThesisDelete(BaseModel):
    isActive: bool = False
    deletedOn: datetime = datetime.now()

class ThesisResponse(ThesisBase):
    thesisId: int