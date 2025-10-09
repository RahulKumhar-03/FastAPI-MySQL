from sqlalchemy import Column, Integer, DateTime, Boolean, String, CHAR, ForeignKey
from database import Base
from datetime import datetime
import uuid
from pydantic import BaseModel

class Honor(Base):
    __tablename__ = 'honor'

    honorId = Column(Integer, primary_key=True, index=True)
    honorName = Column(String(100), nullable=False)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    createdOn = Column(DateTime, default=datetime.now())
    changedBy = Column(Integer,ForeignKey('user.userId'), nullable=True)
    changedOn = Column(DateTime, nullable=True, onupdate=datetime.now())
    deletedBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    deletedOn = Column(DateTime, nullable=True)

class HonorBase(BaseModel):
    honorName: str

class HonorDelete(BaseModel):
    isActive: bool = False
    deletedOn: datetime = datetime.now()

class HonorResponse(HonorBase):
    honorId: int