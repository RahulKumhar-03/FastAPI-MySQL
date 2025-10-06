from sqlalchemy import Column, Integer, Date, Boolean, String, CHAR
from database import Base
from datetime import datetime, date
import uuid
from pydantic import BaseModel

class Honor(Base):
    __tablename__ = 'honor'

    honorId = Column(Integer, primary_key=True, index=True)
    honorName = Column(String(100), nullable=False)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(String(50), nullable=True, default='admin')
    createdOn = Column(Date, default=datetime.now())
    changedBy = Column(String(50), nullable=True)
    changedOn = Column(Date, nullable=True)
    deletedBy = Column(String(50), nullable=True)
    deletedOn = Column(Date, nullable=True)

class HonorBase(BaseModel):
    honorName: str

class HonorCreate(HonorBase):
    createdBy: str
    createdOn: date

class HonorUpdate(HonorBase):
    isActive: bool
    changedBy: str
    changedOn: date

class HonorResponse(HonorBase):
    honorId: int