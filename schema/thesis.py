from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean, String, CHAR, Float
from database import Base
from datetime import datetime, date
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
    createdBy = Column(String(50), nullable=True, default='admin')
    createdOn = Column(Date, default=datetime.now())
    changedBy = Column(String(50), nullable=True)
    changedOn = Column(Date, nullable=True)
    deletedBy = Column(String(50), nullable=True)
    deletedOn = Column(Date, nullable=True)

class ThesisBase(BaseModel):
    title: str 
    advisor: str
    grade: str
    published: bool
    citations: float
    abstract: str

class ThesisCreate(ThesisBase):
    degreeId: int
    createdBy: str
    createdOn: date

class ThesisUpdate(ThesisBase):
    isActive: bool
    changedBy: str
    changedOn: date