from sqlalchemy import Column, Integer, DateTime, Boolean, String, CHAR, ForeignKey
from database import Base
from datetime import datetime
import uuid
from pydantic import BaseModel

class SkillValidated(Base):
    __tablename__ = 'skillvalidated'

    skillValidatedId = Column(Integer, primary_key=True, index=True)
    skillName = Column(String(100), nullable=False)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    createdOn = Column(DateTime, default=datetime.now())
    changedBy = Column(Integer,ForeignKey('user.userId'), nullable=True)
    changedOn = Column(DateTime, nullable=True, onupdate=datetime.now())
    deletedBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    deletedOn = Column(DateTime, nullable=True)

class SkillValidatedBase(BaseModel):
    skillName: str

class SkillValidatedDelete(BaseModel):
    isActive: bool = False
    deletedOn: datetime = datetime.now()

class SkillValidatedResponse(SkillValidatedBase):
    skillValidatedId: int