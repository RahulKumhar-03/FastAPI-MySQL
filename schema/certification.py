from sqlalchemy import Column, Integer, ForeignKey, Boolean, String, CHAR, DateTime, Float
from database import Base
from datetime import datetime, date
import uuid
from pydantic import BaseModel
from typing import Optional

class Certification(Base):
    __tablename__ = 'certification'

    certificationId = Column(Integer, primary_key=True, index=True)
    educationId = Column(Integer, ForeignKey('education.educationId'), nullable=False)
    certificateName = Column(String(100), nullable=False)
    certificateIssuer = Column(String(100), nullable=False)
    issueDate = Column(DateTime, nullable=False)
    expiryDate = Column(DateTime, nullable=False)
    credentialId = Column(String(100), nullable=False)
    verified = Column(Boolean, nullable=False)
    certificateLevel = Column(String(100), nullable=False)
    certificateStatus = Column(String(100), nullable=True)
    examScore = Column(Float, nullable=True)
    passingScore = Column(Float, nullable=True)
    preparationTime = Column(Float, nullable=True)
    renewalRequired = Column(Boolean, nullable=True, default=False)
    renewalPending = Column(Boolean, nullable=True, default=False)
    ceuRequired = Column(Float, nullable=True)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    createdOn = Column(DateTime, default=datetime.now())
    changedBy = Column(Integer,ForeignKey('user.userId'), nullable=True)
    changedOn = Column(DateTime, nullable=True, onupdate=datetime.now())
    deletedBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    deletedOn = Column(DateTime, nullable=True)

class CertificationBase(BaseModel):
    certificateName: str
    certificateIssuer: str
    issueDate: date
    expiryDate: date
    credentialId: str
    verified: bool
    certificateLevel: str
    certificateStatus: Optional[str]
    examScore: Optional[float]
    passingScore: Optional[float]
    preparationTime: Optional[float]
    renewalRequired: Optional[bool]
    renewalPending: Optional[bool]
    ceuRequired: Optional[float]

class CertificationCreate(CertificationBase):
    educationId: int

class CertificationDelete(BaseModel):
    isActive: bool = False
    deletedOn: datetime = datetime.now()

class CertificationResponse(CertificationBase):
    certificationId: int