from fastapi import APIRouter, Depends, HTTPException, status
from database import db_dependency
from services import user_service as UserService
from schema.user import UserUpdate, UserCreate, UserResponse, UserDelete
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from services.auth_service import authenticate_user, create_access_token, get_current_user

router = APIRouter()

user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get("/", response_model=list[UserResponse])
async def getUsers(db: db_dependency, user: user_dependency):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User Not Authorized.')
    
    return UserService.getUsers(db)

@router.post("/register-user")
async def createUser(new_user: UserCreate, db: db_dependency, user: user_dependency):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User Not Authorized.')
    
    return UserService.createUser(new_user, db)

@router.put("/{userId}")
async def updateUser(userId: int, updated_user: UserUpdate, db: db_dependency, user: user_dependency):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User Not Authenticated.')
    
    return UserService.updateUser(userId, updated_user, db)

@router.delete("/{userId}")
async def deleteUser(userId: int, user_delete: UserDelete, db: db_dependency, user: user_dependency):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User Not Authenticated.')
    
    return UserService.deleteUser(userId, user_delete, db)

@router.post('/login')
async def login_user(user: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = authenticate_user(user.username, user.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User Not Found.')
    
    token = create_access_token(user.email, user.userId)

    return {'access_token':token, 'token_type':'bearer'}
    
@router.get('/get-current-user')
def get_currentUser(user: user_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Authentication Failed')
    
    return {"User":user}



