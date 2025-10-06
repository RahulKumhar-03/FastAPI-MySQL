from fastapi import APIRouter
from database import db_dependency
from services import user_service as UserService
from schema.user import UserUpdate, UserBase, UserResponse, UserDelete

router = APIRouter()

@router.get("/", response_model=list[UserResponse])
async def getUsers(db: db_dependency):
    return UserService.getUsers(db)

@router.post("/")
async def createUser(new_user: UserBase, db: db_dependency):
    return UserService.createUser(new_user, db)

@router.put("/{userId}")
async def updateUser(userId: int, updated_user: UserUpdate, db: db_dependency):
    return UserService.updateUser(userId, updated_user, db)

@router.delete("/{userId}")
async def deleteUser(userId: int, user_delete: UserDelete, db: db_dependency):
    return UserService.deleteUser(userId, user_delete, db)
