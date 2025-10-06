from database import Base
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel, Field, validator

class UserAuth(Base):

    __tablename__ = 'user_auth'
    authId = Column(Integer, primary_key=True, index=True)
    userEmail = Column(String(100), nullable=False, unique=True)
    hashed_password = Column(String(500), nullable=False)

class UserRegister(BaseModel):
    userEmail: str

    @validator('userEmail')
    def email_validator(cls, value: str):
        if '@' not in value:
            raise ValueError('Invalid Email Address.')
        return value
    
    password: str = Field(min_length=8)

    @validator('password')
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

    @validator('confirmPassword')
    def password_matching(cls, value, values):
        if 'password' in values and value  != values['password']:
            raise ValueError('Password do not match.')
        return value
    
