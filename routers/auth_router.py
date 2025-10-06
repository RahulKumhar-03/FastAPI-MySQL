from datetime import timedelta, datetime
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from schema.userAuth import UserAuth, UserRegister
from typing import Annotated
from passlib.context import CryptContext
from jose import jwt, JWTError
from fastapi import APIRouter, status, Depends, HTTPException
from database import db_dependency

router = APIRouter()

SECRET_KEY = 'my_secret_key'
ALGORITHM = 'HS256'

pwd_context = CryptContext(schemes=["argon2"], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/login')

@router.post('/register', status_code=status.HTTP_201_CREATED)
async def user_registeration(user_register: UserRegister, db: db_dependency):
    create_user_model = UserAuth(
        userEmail = user_register.userEmail,
        hashed_password = pwd_context.hash(user_register.password)
    )
    db.add(create_user_model)
    db.commit()
    return {'message':'User Registered Successfully.'}

@router.post('/login')
async def login_user(user: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = authenticate_user(user.username, user.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')
    
    token = create_access_token(user.userEmail, user.authId, timedelta(minutes=20))

    return {'access_token':token, 'token_type':'bearer'}

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        userEmail: str = payload.get('sub')
        userId: int = payload.get('id')
        if userEmail is None or userId is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user.')
        return {'userEmail':userEmail, 'id': userId}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user.')
    
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get('/current-user')
def get_currentUser(user: user_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Authentication Failed')
    return {"User":user}

def create_access_token(email: str, user_id: int, expires_delta: timedelta):
    encode = {'sub': email, 'id': user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp':expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

def authenticate_user(email: str, password: str, db: db_dependency):
    db_user = db.query(UserAuth).filter(UserAuth.userEmail == email).first()

    if not db_user: 
        return False
    if not pwd_context.verify(password, db_user.hashed_password):
        return False
    return db_user