from fastapi import APIRouter,Depends,HTTPException,Response,status,UploadFile
from src.showroom.schemas import AddressCreate,AddressModel,ShopCreate,ShopModel,ShopUpdate,CategoryCreate,CategoryUpdate,CategoryModel
from src.core.container import Container
from src.showroom.models import Address,Shop,Category
from src.core.repositories import ModelRepositories
from src.showroom.queries import ShopRepositories
from fastapi.responses import JSONResponse
from src.core.config import fomatter


address_router = APIRouter(prefix='/address',tags=['address'])
shop_router = APIRouter(prefix='/shop',tags=['shop'])
shop_category_router = APIRouter(prefix='/shop/category',tags=['shop_category'])



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

#shop category APIs

@shop_category_router.post('')
def create_shop_category(shop_category:CategoryCreate=Depends(),logo_image:UploadFile | None = None):
    c = ModelRepositories(model_type=Category)
    shop_category = shop_category.dict()
    
    if logo_image:
        logo_image_path = c.file_upload_and_save(logo_image,'category')
        shop_category['logo_url'] = logo_image_path

    the_shop_category = c.create(shop_category)
    return JSONResponse(**fomatter.success_post_response('shop_category',the_shop_category))

@shop_category_router.get('')
def get_shop_category_by_id(id:int):
    c = ModelRepositories(model_type=Category)
    the_shop_category = c.get_by_id(id=id)
    if the_shop_category is None:
        return JSONResponse(**fomatter.error_get_by_id_response('shop_category',id))
    return JSONResponse(**fomatter.success_get_response(the_shop_category,CategoryModel))

@shop_category_router.get('/all')
def get_all_shop_categories():
    c = ModelRepositories(model_type=Category)
    the_shop_categories = c.get_all()
    if the_shop_categories is None:
        return JSONResponse(**fomatter.error_get_by_id_response('shop_category'))
    return JSONResponse(**fomatter.success_get_all_response(the_shop_categories))

@shop_category_router.delete('')
def delete_shop_category_by_id(id:int):
    c = ModelRepositories(model_type=Category)
    the_shop_category = c.get_by_id(id=id)
    if the_shop_category is None:
        return JSONResponse(**fomatter.error_get_by_id_response('shop_category',id))
    c.delete_object(the_shop_category)
    return JSONResponse(**fomatter.success_delete_response('shop_category',id))

@shop_category_router.put('')
def update_shop_category_by_id(shop_category:CategoryUpdate=Depends(),logo_image:UploadFile | None = None):
    c = ModelRepositories(model_type=Category)
    the_shop_category = c.get_by_id(id=id)
    if the_shop_category is None:
        return JSONResponse(**fomatter.error_get_by_id_response('shop_category',id))
    if logo_image:
        logo_image_path = c.file_upload_and_save(logo_image,'shop_category')
        shop_category = shop_category.dict()
        shop_category['logo_url'] = logo_image_path

    the_shop_category = c.update_object(the_shop_category,data=shop_category)
    return JSONResponse(**fomatter.success_update_response(the_shop_category,'shop_category',id))

# shop APIs
@shop_router.post('')
def create_shop(shop:ShopCreate=Depends(),banner_image:UploadFile | None = None,logo_image:UploadFile | None = None):
    print('hii')
    c = ModelRepositories(model_type=Shop)
    shop = shop.dict()
    if banner_image:
        banner_image_path = c.file_upload_and_save(banner_image,'shop')
        shop['banner_url'] = banner_image_path
    if logo_image:
        logo_image_path = c.file_upload_and_save(logo_image,'shop')
        shop['logo_url'] = logo_image_path

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
@shop_router.get('/by/category/id')
def get_shop_by_category(category_id:int):
    shop_obj = ShopRepositories(model_type=Shop)
    the_shops = shop_obj.shop_by_category_id(category_id=category_id)
    if the_shops is None:
        return JSONResponse(**fomatter.error_get_by_id_response('shop',id))
    return JSONResponse(**fomatter.success_get_all_response(the_shops))


@shop_router.put('')
def update_shop_by_id(shop:ShopUpdate=Depends(),banner_image:UploadFile | None = None,logo_image:UploadFile | None = None):
    c = ModelRepositories(model_type=Shop)
    the_shop = c.get_by_id(id=id)
    if the_shop is None:
        return JSONResponse(**fomatter.error_get_by_id_response('shop',id))
    if banner_image:
        banner_image_path = c.file_upload_and_save(banner_image,'shop')
        shop = shop.dict()
        shop['image_url'] = banner_image_path
    if logo_image:
        logo_image_path = c.file_upload_and_save(logo_image,'shop')
        shop = shop.dict()
        shop['logo_url'] = logo_image_path

    the_shop = c.update_object(the_shop,data=shop)
    return JSONResponse(**fomatter.success_update_response(the_shop,'shop',id))


