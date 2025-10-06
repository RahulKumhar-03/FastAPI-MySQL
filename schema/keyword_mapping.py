from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean, String, CHAR, DateTime, Float
from database import Base
from datetime import datetime, date
import uuid
from pydantic import BaseModel

class KeywordMapping(Base):
    __tablename__ = 'keywordmapping'

    keywordMappingId = Column(Integer, primary_key=True, index=True)
    thesisId = Column(Integer, ForeignKey('thesis.thesisId'), nullable=False)
    keywordId = Column(Integer, ForeignKey('keyword.keywordId'), nullable=False)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(String(50), nullable=True, default='admin')
    createdOn = Column(Date, default=datetime.now())
    changedBy = Column(String(50), nullable=True)
    changedOn = Column(Date, nullable=True)
    deletedBy = Column(String(50), nullable=True)
    deletedOn = Column(Date, nullable=True)

class KeywordMappingBase(BaseModel):
    thesisId: int
    keywordId: int

class KeywordMappingCreate(KeywordMappingBase):
    createdBy: str
    createdOn: date

class KeywordMappingUpdate(KeywordMappingBase):
    isActive: bool
    changedBy: str
    changedOn: date

class KeywordMappingDelete(BaseModel):
    isActive: bool = False
    deletedBy: str
    deletedOn: datetime

class KeywordMappingResponse(KeywordMappingBase):
    keywordMappingId: int