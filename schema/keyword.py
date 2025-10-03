from sqlalchemy import Column, Integer, Date, Boolean, String, CHAR
from database import Base
from datetime import datetime, date
import uuid
from pydantic import BaseModel

class Keyword(Base):
    __tablename__ = 'keyword'

    keywordId = Column(Integer, primary_key=True, index=True)
    keyword = Column(String(100), nullable=False)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(String(50), nullable=True, default='admin')
    createdOn = Column(Date, default=datetime.now())
    changedBy = Column(String(50), nullable=True)
    changedOn = Column(Date, nullable=True)
    deletedBy = Column(String(50), nullable=True)
    deletedOn = Column(Date, nullable=True)

class KeywordBase(BaseModel):
    keyword: str

class KeywordCreate(KeywordBase):
    createdBy: str
    createdOn: date

class KeywordUpdate(KeywordBase):
    isActive: bool
    changedBy: str
    changedOn: date