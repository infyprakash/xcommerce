from fastapi import APIRouter,Depends,HTTPException,Response,status
from src.user.schemas import UserCreate,UserModel ,UserLogin
from src.core.container import Container
from src.user.models import User
from src.core.repositories import ModelRepositories
from src.user.queries import UserRepositories
from src.user.utils import get_password_hash,verify_password,create_access_token

from fastapi.responses import JSONResponse
from src.core.config import fomatter
from src.user.utils import get_current_user

user_router = APIRouter(prefix='/user',tags=['user'])

# user APIs
@user_router.post('/register')
def create_user(user:UserCreate):
    user = user.dict()
    print(user)
    u = UserRepositories(model_type=User)
    the_user = u.check_user_exists(username=user['phone_no'])
    if the_user:
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE,content={'content':{'message':f'User with username {user["phone_no"]} already exists'}})
    if user['password'] != user['confirm_password']:
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE,content={'content':{'message':f'{user["password"]} and {user["confirm_password"]} do not match'}})
    user['hashed_password'] = get_password_hash(password=user['password'])
    user.pop('password')
    user.pop('confirm_password')
    the_user = u.create(user)
    return JSONResponse(**fomatter.success_post_response('user',the_user))

import json
@user_router.post('/login')
def get_access_token(user:UserLogin):
    u = UserRepositories(model_type=User)
    the_user = u.check_user_exists(username=user.phone_no)
    print(the_user.__dict__)
    if not the_user:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content={'content':{'message':f'User with username {user.phone_no} does not  exists'}})
    if not verify_password(plain_password=user.password,hashed_password=the_user.hashed_password):
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content={'content':{'message':'Incorrect username or password'}})
    # data = {}
    # data['id'] = the_user.id
    # data['uuid'] = str(the_user.uuid)
    # data['full_name'] = the_user.full_name
    # data['email'] = the_user.email 
    # data['phone_no'] = the_user.phone_no
    # data['is_superuser'] = the_user.is_superuser
    # data['is_staff'] = the_user.is_staff
    access_token = create_access_token(data={'sub':str(the_user.id)})
    return JSONResponse(status_code=status.HTTP_201_CREATED,content={'content':{'message':'Login success','access_token':access_token,'token_type':'bearer'}})


    
@user_router.get('')
def get_user_by_id(id:int):
    c = ModelRepositories(model_type=User)
    the_user = c.get_by_id(id=id)
    if the_user is None:
        return JSONResponse(**fomatter.error_get_by_id_response('user',id))
    return JSONResponse(**fomatter.success_get_response(the_user,UserModel))


@user_router.get('/all')
def get_all_users():
    c = ModelRepositories(model_type=User)
    the_users = c.get_all()
    if the_users is None:
        return JSONResponse(**fomatter.error_get_by_id_response('user'))
    return JSONResponse(**fomatter.success_get_all_response(the_users))

@user_router.delete('')
def delete_user_by_id(id:int):
    c = ModelRepositories(model_type=User)
    the_user = c.get_by_id(id=id)
    if the_user is None:
        return JSONResponse(**fomatter.error_get_by_id_response('user',id))
    c.delete_object(the_user)
    return JSONResponse(**fomatter.success_delete_response('user',id))

@user_router.put('')
def update_user_by_id(id:int,user:UserCreate):
    c = ModelRepositories(model_type=User)
    the_user = c.get_by_id(id=id)
    if the_user is None:
        return JSONResponse(**fomatter.error_get_by_id_response('user',id))
    the_user = c.update_object(the_user,data=user)
    return JSONResponse(**fomatter.success_update_response(the_user,'user',id))

@user_router.get('/me')
def get_me(user:User=Depends(get_current_user)):
    return user


