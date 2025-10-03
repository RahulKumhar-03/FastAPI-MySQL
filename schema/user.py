from sqlalchemy import Column, Integer, String, Boolean, Date, CHAR
from database import Base
from datetime import datetime, date
import uuid
from pydantic import BaseModel

class User(Base):
    __tablename__ = 'user'

    userId = Column(Integer, primary_key=True, index=True)
    firstName = Column(String(50), nullable=False)
    userName = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(String(50), nullable=True, default='admin')
    createdOn = Column(Date, default=datetime.now())
    changedBy = Column(String(50), nullable=True)
    changedOn = Column(Date, nullable=True)
    deletedBy = Column(String(50), nullable=True)
    deletedOn = Column(Date, nullable=True)

class UserBase(BaseModel):
    firstName: str
    userName: str
    email: str

class UserUpdate(UserBase):
    isActive:bool
    changedBy: str
    changedOn: date
