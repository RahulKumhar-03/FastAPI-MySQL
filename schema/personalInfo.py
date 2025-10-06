from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean, String, CHAR
from database import Base
from datetime import datetime, date
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
    createdBy = Column(String(50), nullable=True, default='admin')
    createdOn = Column(Date, default=datetime.now())
    changedBy = Column(String(50), nullable=True)
    changedOn = Column(Date, nullable=True)
    deletedBy = Column(String(50), nullable=True)
    deletedOn = Column(Date, nullable=True)

class PersonalInfoBase(BaseModel):
    middleName: str
    workPhone: str
    workEmail: str

class PersonalInfoCreate(PersonalInfoBase):
    contactId: int
    userId: int
    createdBy: str
    createdOn: date

class PersonalInfoUpdate(PersonalInfoBase):
    isActive: bool
    changedBy: str
    changedOn: date

class PersonalInfoDelete(BaseModel):
    isActive: bool = False
    deletedBy: str
    deletedOn: datetime

class PersonalInfoResponse(PersonalInfoBase):
    personalInfoId: int

