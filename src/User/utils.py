import os
from datetime import datetime,timedelta
from typing import Union,Any,Annotated
from passlib.context import CryptContext
from src.core.config import setting
from jose import jwt,JWTError
from fastapi.security import OAuth2PasswordBearer,OAuth2AuthorizationCodeBearer,HTTPBearer
from fastapi import Depends,status,HTTPException
from src.user.queries import UserRepositories
from src.user.models import User


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token",scheme_name='JWT')
# oauth2_scheme = OAuth2AuthorizationCodeBearer(tokenUrl="token",authorizationUrl='login')
oauth2_scheme = HTTPBearer()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password:str)->str:
    return pwd_context.hash(password)

def create_access_token(data:dict,expires_delta:int| None=0):
    print(type(setting.JWT_SECRET_KEY))
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=int(setting.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({'exp':expire})
    encoded_jwt = jwt.encode(to_encode, setting.JWT_SECRET_KEY, algorithm=setting.ALGORITHM)
    return encoded_jwt


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token.credentials, setting.JWT_SECRET_KEY, algorithms=[setting.ALGORITHM])
        print(payload)
        user_id = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    u = UserRepositories(model_type=User)
    the_user = u.get_user_by_id(id=int(user_id))
    if the_user is None:
        raise credentials_exception
    return the_user







