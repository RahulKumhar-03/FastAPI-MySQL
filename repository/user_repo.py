from schema.user import User, UserBase, UserUpdate
from database import db_dependency
from fastapi import HTTPException, status


def create_user(user: UserBase, db: db_dependency):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    return db_user

def get_users(db: db_dependency):
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

def delete_user(userId: int, db: db_dependency):
    user = db.query(User).filter(User.userId == userId).first()

    db.delete(user)
    db.commit()
    return {"message":"User Deleted Successfully."}