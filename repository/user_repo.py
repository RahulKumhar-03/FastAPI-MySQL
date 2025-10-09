from schema.user import User, UserCreate, UserUpdate, UserResponse, UserDelete
from database import db_dependency
from fastapi import HTTPException, status
from services.auth_service import pwd_context

def create_user(user: UserCreate, db: db_dependency, current_user):
    db_user = User(
        firstName = user.firstName,
        userName = user.userName,
        email = user.email, 
        hashed_password = pwd_context.hash(user.password),
        createdBy = current_user["userId"]
    )
    db.add(db_user)
    db.commit()
    return {'message':'User Registered Successfully.'}

def get_users(db: db_dependency) -> list[UserResponse]:
    users = db.query(User).all()
    return users

def update_user(userId: int, user_updated: UserUpdate, db: db_dependency, currentUser):
    user = db.query(User).filter(User.userId == userId).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    
    user_updated_dict = user_updated.model_dump()

    for key, value in user_updated_dict.items():
        setattr(user, key, value)

    user.changedBy = currentUser["userId"]
    
    db.commit()
    return user

def delete_user(userId: int, user_delete: UserDelete, db: db_dependency, currentUser):
    db_user = db.query(User).filter(User.userId == userId).first()

    user_delete_dict = dict(user_delete)

    for key, value in user_delete_dict.items():
        setattr(db_user, key, value)

    db_user.deletedBy = currentUser["userId"]

    db.commit()
    return {"message":"User Deleted Successfully."}

def userExists(userId: int, db: db_dependency):
    db_user = db.query(User).filter(userId == User.userId).first()
    
    return db_user

def findUserByEmail(userEmail: str, db):
    db_user = db.query(User).filter(User.email == userEmail).first()

    return db_user

