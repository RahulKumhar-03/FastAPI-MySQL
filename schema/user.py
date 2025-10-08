from sqlalchemy import Column, Integer, String, Boolean, DateTime, CHAR, ForeignKey
from database import Base
from datetime import datetime
import uuid
from pydantic import BaseModel, ValidationInfo, field_validator, Field

class User(Base):
    __tablename__ = 'user'

    userId = Column(Integer, primary_key=True, index=True)
    firstName = Column(String(50), nullable=False)
    userName = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    hashed_password = Column(String(500), nullable=False)
    uiId = Column(CHAR(36), nullable=False, default=str(uuid.uuid4()))
    isActive = Column(Boolean, default=True)
    createdBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    createdOn = Column(DateTime, default=datetime.now())
    changedBy = Column(Integer,ForeignKey('user.userId'), nullable=True)
    changedOn = Column(DateTime, nullable=True, onupdate=datetime.now())
    deletedBy = Column(Integer, ForeignKey('user.userId'), nullable=True)
    deletedOn = Column(DateTime, nullable=True)

class UserBase(BaseModel):
    firstName: str
    userName: str
    email: str
    
    @field_validator('userName')
    def no_continuous_spaces(cls, value: str) -> str:
        if '  ' in value:
            raise ValueError('Username cannot contain continuous spaces')
        return value

    @field_validator('email')
    def email_validator(cls, value: str):
        if '@' not in value:
            raise ValueError('Invalid Email Address.')
        return value
    
class UserCreate(UserBase):
    password: str
    confirmPassword: str

    @field_validator('password')
    def password_validator(cls, value: str):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not any(char.isupper() for char in value):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(char.islower() for char in value):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(char.isdigit() for char in value):
            raise ValueError("Password must contain at least one digit")
        if not any(char in "!@#$%^&*()-_+=" for char in value):
            raise ValueError("Password must contain at least one special character")
        return value
    
    confirmPassword: str

    @field_validator('confirmPassword')
    def password_matching(cls, value: str, info: ValidationInfo):
        if value != info.data['password']:
            raise ValueError('Passwords do not match')
        return value

class UserUpdate(UserBase):
    isActive:bool

class UserDelete(BaseModel):
    isActive: bool = False
    deletedOn: datetime = datetime.now()

class UserResponse(UserBase):
    userId: int
