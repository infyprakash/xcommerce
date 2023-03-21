from fastapi import APIRouter,Depends,HTTPException
from src.catalogue.schemas import ProductCreate,CategoryCreate
from src.core.container import Container
from src.catalogue.models import Category

router = APIRouter(prefix='/catalogue',tags=['catalogue'])

def get_session_object():
    session = Container().db_obj()
    return session

@router.post('/product')
def create_product(catalog:ProductCreate):
    pass

@router.get('/category')
def create_category():
    the_category = Category.query.all()
    return {'message':the_category}

