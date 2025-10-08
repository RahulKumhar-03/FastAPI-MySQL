from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean, String, CHAR, DateTime, Float
from database import Base
from datetime import datetime, date
import uuid
from pydantic import BaseModel

class SkillValidatedMapping(Base):
    __tablename__ = 'skillvalidatedmapping'

    skillValidatedMappingId = Column(Integer, primary_key=True, index=True)
    certificationId = Column(Integer, ForeignKey('certification.certificationId'), nullable=False)
    skillValidatedId = Column(Integer, ForeignKey('skillvalidated.skillValidatedId'), nullable=False)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(String(50), nullable=True, default='admin')
    createdOn = Column(Date, default=datetime.now())
    changedBy = Column(String(50), nullable=True)
    changedOn = Column(Date, nullable=True)
    deletedBy = Column(String(50), nullable=True)
    deletedOn = Column(Date, nullable=True)

class SkillValidatedMappingBase(BaseModel):
    certificationId: int
    skillValidatedId: int

class SkillValidatedMappingCreate(SkillValidatedMappingBase):
    createdBy: str

class SkillValidatedMappingUpdate(SkillValidatedMappingBase):
    isActive: bool = False
    changedBy: str
    changedOn: datetime

class SkillValidatedMappingDelete(BaseModel):
    isActive: bool
    deletedBy: str
    deletedOn: datetime

class SkillValidatedMappingResponse(SkillValidatedMappingBase):
    skillValidatedMappingId: int