from repository import user_repo as UserRepository
from database import db_dependency
from schema.user import User, UserCreate, UserUpdate, UserDelete
from fastapi import HTTPException, status

def getUsers(db: db_dependency):
    return UserRepository.get_users(db);

def createUser(new_user: UserCreate, db: db_dependency):
    return UserRepository.create_user(new_user, db)

def updateUser(userId: int, updated_user: UserUpdate, db: db_dependency):
    return UserRepository.update_user(userId, updated_user, db)

def deleteUser(userId: int, user_delete: UserDelete,  db: db_dependency):
    user = UserRepository.userExists(userId, db)
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return UserRepository.delete_user(userId, user_delete, db)
    