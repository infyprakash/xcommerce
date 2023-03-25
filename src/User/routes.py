from fastapi import APIRouter,Depends,HTTPException,Response,status
from src.user.schemas import UserCreate,UserModel 
from src.core.container import Container
from src.user.models import User
from src.core.repositories import ModelRepositories
from fastapi.responses import JSONResponse
from src.core.config import fomatter

user_router = APIRouter(prefix='/user',tags=['user'])

# user APIs
@user_router.post('')
def create_user(user:UserCreate):
    c = ModelRepositories(model_type=User)
    the_user = c.create(user)
    return JSONResponse(**fomatter.success_post_response('user',the_user))

@user_router.get('')
def get_user_by_id(id:int):
    c = ModelRepositories(model_type=User)
    the_user = c.get_by_id(id=id)
    if the_user is None:
        return JSONResponse(**fomatter.error_get_by_id_response('user',id))
    return JSONResponse(**fomatter.success_get_response(the_user,UserModel))

@user_router.get('/all')
def get_all_categories():
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


