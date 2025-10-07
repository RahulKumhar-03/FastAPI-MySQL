from schema.user import User, UserCreate, UserUpdate, UserResponse, UserDelete
from database import db_dependency
from fastapi import HTTPException, status
from services.auth_service import pwd_context

def create_user(user: UserCreate, db: db_dependency):
    db_user = User(
        firstName = user.firstName,
        userName = user.userName,
        email = user.email, 
        hashed_password = pwd_context.hash(user.password)
    )
    db.add(db_user)
    db.commit()
    return {'message':'User Registered Successfully.'}

def get_users(db: db_dependency) -> list[UserResponse]:
    users = db.query(User).all()
    return users

def update_user(userId: int, user_updated: UserUpdate, db: db_dependency):
    user = db.query(User).filter(User.userId == userId).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")

    for key, value in user_updated.dict(exclude_unset=True).items():
        setattr(user, key, value)
    
    db.commit()
    return user

def delete_user(userId: int, user_delete: UserDelete, db: db_dependency):
    db_user = db.query(User).filter(User.userId == userId).first()

    for key, value in user_delete.dict(exclude_unset=True).items():
        setattr(db_user, key, value)

    db.commit()
    return {"message":"User Deleted Successfully."}
