from sqlalchemy import Column, Integer, DateTime, ForeignKey, Boolean, String, CHAR
from database import Base
from datetime import datetime
import uuid
from pydantic import BaseModel

class PersonalInfo(Base):
    __tablename__ = 'personalinfo'

    personalInfoId = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey('user.userId'), unique=True, nullable=False)
    contactId = Column(Integer, unique=True, nullable=False)
    middleName = Column(String(100), nullable=False)
    workPhone = Column(String(50), nullable=False)
    workEmail = Column(String(50), nullable=False)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    createdOn = Column(DateTime, default=datetime.now())
    changedBy = Column(Integer,ForeignKey('user.userId'), nullable=True)
    changedOn = Column(DateTime, nullable=True, onupdate=datetime.now())
    deletedBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    deletedOn = Column(DateTime, nullable=True)

class PersonalInfoBase(BaseModel):
    middleName: str
    workPhone: str
    workEmail: str

class PersonalInfoCreate(PersonalInfoBase):
    contactId: int

class PersonalInfoDelete(BaseModel):
    isActive: bool = False
    deletedOn: datetime = datetime.now()

class PersonalInfoResponse(PersonalInfoBase):
    personalInfoId: int

