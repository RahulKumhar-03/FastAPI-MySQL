from passlib.context import CryptContext
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from typing import Annotated
from schema.user import User
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["argon2"], deprecated='auto')

SECRET_KEY = 'my_secret_key'
ALGORITHM = 'HS256'

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='users/login')

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

def create_access_token(email: str, user_id: int, expires_delta: timedelta):
    encode = {'sub': email, 'id': user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp':expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

def authenticate_user(email: str, password: str, db):
    db_user = db.query(User).filter(User.email == email).first()

    if not db_user: 
        return False

    if not pwd_context.verify(password, db_user.hashed_password):
        return False
    
    return db_user