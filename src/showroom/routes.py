from fastapi import APIRouter,Depends,HTTPException,Response,status
from src.showroom.schemas import AddressCreate,AddressModel,ShopCreate,ShopModel
from src.core.container import Container
from src.showroom.models import Address,Shop
from src.core.repositories import ModelRepositories
from fastapi.responses import JSONResponse
from src.core.config import fomatter


address_router = APIRouter(prefix='/address',tags=['address'])
shop_router = APIRouter(prefix='/shop',tags=['shop'])

# address APIs
@address_router.post('')
def create_address(address:AddressCreate):
    c = ModelRepositories(model_type=Address)
    the_address = c.create(address)
    return JSONResponse(**fomatter.success_post_response('address',the_address))

@address_router.get('')
def get_address_by_id(id:int):
    c = ModelRepositories(model_type=Address)
    the_address = c.get_by_id(id=id)
    if the_address is None:
        return JSONResponse(**fomatter.error_get_by_id_response('address',id))
    return JSONResponse(**fomatter.success_get_response(the_address,AddressModel))

@address_router.get('/all')
def get_all_addresses():
    c = ModelRepositories(model_type=Address)
    the_addresses = c.get_all()
    if the_addresses is None:
        return JSONResponse(**fomatter.error_get_by_id_response('address'))
    return JSONResponse(**fomatter.success_get_all_response(the_addresses))

@address_router.delete('')
def delete_address_by_id(id:int):
    c = ModelRepositories(model_type=Address)
    the_address = c.get_by_id(id=id)
    if the_address is None:
        return JSONResponse(**fomatter.error_get_by_id_response('address',id))
    c.delete_object(the_address)
    return JSONResponse(**fomatter.success_delete_response('address',id))

@address_router.put('')
def update_address_by_id(id:int,address:AddressCreate):
    c = ModelRepositories(model_type=Address)
    the_address = c.get_by_id(id=id)
    if the_address is None:
        return JSONResponse(**fomatter.error_get_by_id_response('address',id))
    the_address = c.update_object(the_address,data=address)
    return JSONResponse(**fomatter.success_update_response(the_address,'address',id))


# shop APIs
@shop_router.post('')
def create_shop(shop:ShopCreate):
    c = ModelRepositories(model_type=Shop)
    the_shop = c.create(shop)
    return JSONResponse(**fomatter.success_post_response('shop',the_shop))

@shop_router.get('')
def get_shop_by_id(id:int):
    c = ModelRepositories(model_type=Shop)
    the_shop = c.get_by_id(id=id)
    if the_shop is None:
        return JSONResponse(**fomatter.error_get_by_id_response('shop',id))
    return JSONResponse(**fomatter.success_get_response(the_shop,ShopModel))

@shop_router.get('/all')
def get_all_shops():
    c = ModelRepositories(model_type=Shop)
    the_shops = c.get_all()
    if the_shops is None:
        return JSONResponse(**fomatter.error_get_by_id_response('shop'))
    return JSONResponse(**fomatter.success_get_all_response(the_shops))

@shop_router.delete('')
def delete_shop_by_id(id:int):
    c = ModelRepositories(model_type=Shop)
    the_shop = c.get_by_id(id=id)
    if the_shop is None:
        return JSONResponse(**fomatter.error_get_by_id_response('shop',id))
    c.delete_object(the_shop)
    return JSONResponse(**fomatter.success_delete_response('shop',id))

@shop_router.put('')
def update_shop_by_id(id:int,shop:ShopCreate):
    c = ModelRepositories(model_type=Shop)
    the_shop = c.get_by_id(id=id)
    if the_shop is None:
        return JSONResponse(**fomatter.error_get_by_id_response('shop',id))
    the_shop = c.update_object(the_shop,data=shop)
    return JSONResponse(**fomatter.success_update_response(the_shop,'shop',id))


