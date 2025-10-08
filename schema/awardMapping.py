from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean, String, CHAR, DateTime, Float
from database import Base
from datetime import datetime
import uuid
from pydantic import BaseModel

class AwardMapping(Base):
    __tablename__ = 'awardmapping'

    awardMappingId = Column(Integer, primary_key=True, index=True)
    awardId = Column(Integer, ForeignKey('award.awardId'), nullable=False)
    degreeId = Column(Integer, ForeignKey('degree.degreeId'), nullable=False)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(String(50), nullable=True, default='admin')
    createdOn = Column(Date, default=datetime.now())
    changedBy = Column(String(50), nullable=True)
    changedOn = Column(Date, nullable=True)
    deletedBy = Column(String(50), nullable=True)
    deletedOn = Column(Date, nullable=True)

class AwardMappingBase(BaseModel):
    awardId: int
    degreeId: int

class awardMappingCreate(AwardMappingBase):
    createdBy: str

class AwardMappingUpdate(AwardMappingBase):
    isActive: bool
    changedBy: str
    changedOn: datetime

class AwardMappingDelete(BaseModel):
    isActive: bool = False
    deletedBy: str
    deletedOn: datetime

class AwardMappingResponse(AwardMappingBase):
    awardMappingId: int