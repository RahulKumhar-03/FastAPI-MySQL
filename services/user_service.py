from repository import user_repo as UserRepository
from database import db_dependency
from schema.user import User, UserBase, UserUpdate
from fastapi import HTTPException, status

def getUsers(db: db_dependency):
    return UserRepository.get_users(db);

def createUser(new_user: UserBase, db: db_dependency):
    return UserRepository.create_user(new_user, db)

def updateUser(userId: int, updated_user: UserUpdate, db: db_dependency):
    return UserRepository.update_user(userId, updated_user, db)

def deleteUser(userId: int, db: db_dependency):
    user = db.query(User).filter(User.userId == userId).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    
    return UserRepository.delete_user(userId, db)
    