from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean, String, CHAR, DateTime, Float
from database import Base
from datetime import datetime, date
import uuid
from pydantic import BaseModel

class HonorMapping(Base):
    __tablename__ = 'honormapping'

    honorMappingId = Column(Integer, primary_key=True, index=True)
    honorId = Column(Integer, ForeignKey('honor.honorId'), nullable=False)
    degreeId = Column(Integer, ForeignKey('degree.degreeId'), nullable=False)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(String(50), nullable=True, default='admin')
    createdOn = Column(Date, default=datetime.now())
    changedBy = Column(String(50), nullable=True)
    changedOn = Column(Date, nullable=True)
    deletedBy = Column(String(50), nullable=True)
    deletedOn = Column(Date, nullable=True)

class HonorMappingBase(BaseModel):
    honorId: int
    degreeId: int

class HonorMappingCreate(HonorMappingBase):
    createdBy: str
    createdOn: date

class HonorMappingUpdate(HonorMappingBase):
    isActive: bool
    changedBy: str
    changedOn: date

class HonorMappingDelete(BaseModel):
    isActive: bool = False
    deletedBy: str
    deletedOn: datetime

class HonorMappingResponse(HonorMappingBase):
    honorMappingId: int