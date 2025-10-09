from sqlalchemy import Column, Integer, ForeignKey, Boolean, String, CHAR, DateTime
from database import Base
from datetime import datetime
import uuid
from pydantic import BaseModel

class SkillValidatedMapping(Base):
    __tablename__ = 'skillvalidatedmapping'

    skillValidatedMappingId = Column(Integer, primary_key=True, index=True)
    certificationId = Column(Integer, ForeignKey('certification.certificationId'), nullable=False)
    skillValidatedId = Column(Integer, ForeignKey('skillvalidated.skillValidatedId'), nullable=False)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    createdOn = Column(DateTime, default=datetime.now())
    changedBy = Column(Integer,ForeignKey('user.userId'), nullable=True)
    changedOn = Column(DateTime, nullable=True, onupdate=datetime.now())
    deletedBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    deletedOn = Column(DateTime, nullable=True)

class SkillValidatedMappingBase(BaseModel):
    certificationId: int
    skillValidatedId: int

class SkillValidatedMappingDelete(BaseModel):
    isActive: bool = False
    deletedOn: datetime = datetime.now()

class SkillValidatedMappingResponse(SkillValidatedMappingBase):
    skillValidatedMappingId: int