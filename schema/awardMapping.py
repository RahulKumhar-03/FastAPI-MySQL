from sqlalchemy import Column, Integer, ForeignKey, Boolean, CHAR, DateTime
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
    createdBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    createdOn = Column(DateTime, default=datetime.now())
    changedBy = Column(Integer,ForeignKey('user.userId'), nullable=True)
    changedOn = Column(DateTime, nullable=True, onupdate=datetime.now())
    deletedBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    deletedOn = Column(DateTime, nullable=True)

class AwardMappingBase(BaseModel):
    awardId: int
    degreeId: int

class AwardMappingDelete(BaseModel):
    isActive: bool = False
    deletedOn: datetime = datetime.now()

class AwardMappingResponse(AwardMappingBase):
    awardMappingId: int