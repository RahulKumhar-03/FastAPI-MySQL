from sqlalchemy import Column, Integer, ForeignKey, Boolean, String, CHAR, DateTime
from database import Base
from datetime import datetime
import uuid
from pydantic import BaseModel

class KeywordMapping(Base):
    __tablename__ = 'keywordmapping'

    keywordMappingId = Column(Integer, primary_key=True, index=True)
    thesisId = Column(Integer, ForeignKey('thesis.thesisId'), nullable=False)
    keywordId = Column(Integer, ForeignKey('keyword.keywordId'), nullable=False)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    createdOn = Column(DateTime, default=datetime.now())
    changedBy = Column(Integer,ForeignKey('user.userId'), nullable=True)
    changedOn = Column(DateTime, nullable=True, onupdate=datetime.now())
    deletedBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    deletedOn = Column(DateTime, nullable=True)

class KeywordMappingBase(BaseModel):
    thesisId: int
    keywordId: int

class KeywordMappingDelete(BaseModel):
    isActive: bool = False
    deletedOn: datetime = datetime.now()

class KeywordMappingResponse(KeywordMappingBase):
    keywordMappingId: int