from passlib.context import CryptContext
from jose import JWTError, jwt, ExpiredSignatureError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from typing import Annotated
from datetime import datetime, timedelta
from settings import settings
from repository import user_repo as UserRepo

pwd_context = CryptContext(schemes=["argon2"], deprecated='auto')

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='users/login')

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        userEmail: str = payload.get('sub')
        userId: int = payload.get('id')

        if userEmail is None or userId is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User Not Authenticated.')
        
        return {'userEmail':userEmail, 'id': userId}
    
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired"
        )
    
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User Not Authenticated.')

def create_access_token(email: str, user_id: int):
    encode = {'sub': email, 'id': user_id}
    expires = datetime.utcnow() + timedelta(minutes=1) 
    encode.update({'exp':expires})
    return jwt.encode(encode, settings.secret_key, algorithm = settings.algorithm)

def authenticate_user(email: str, password: str, db):
    db_user = UserRepo.findUserByEmail(email, db)

    if not db_user: 
        return False

    if not pwd_context.verify(password, db_user.hashed_password):
        return False
    
    return db_user