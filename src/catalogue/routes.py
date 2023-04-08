from fastapi import APIRouter,Depends,HTTPException,Response,status,UploadFile,File,Form
from src.catalogue.schemas import ProductCreate,ProductModel,ProductImageCreate,ProductImageModel,ProductImageUpdate
from src.core.container import Container
from src.catalogue.models import Product,ProductImage
from src.core.repositories import ModelRepositories
from fastapi.responses import JSONResponse
from src.core.config import fomatter
from fastapi.encoders import jsonable_encoder
from typing import Optional



# category_router = APIRouter(prefix='/category',tags=['category'])
product_router = APIRouter(prefix='/product',tags=['product'])
product_image_router = APIRouter(prefix='/product/image',tags=['product_image'])


# category APIs
# @category_router.post('')
# def create_category(category:CategoryCreate = Depends(),image:UploadFile | None = None):
#     c = ModelRepositories(model_type=Category)
#     category = category.dict()
#     if image:
#         image_path = c.file_upload_and_save(image,'category')
#         category['image'] = image_path
#     the_category = c.create(category)
#     return JSONResponse(**fomatter.success_post_response('category',the_category))

# @category_router.get('')
# def get_category_by_id(id:int):
#     c = ModelRepositories(model_type=Category)
#     the_category = c.get_by_id(id=id)
#     if the_category is None:
#         return JSONResponse(**fomatter.error_get_by_id_response('category',id))
#     return JSONResponse(**fomatter.success_get_response(the_category,CategoryModel))

# @category_router.get('/all')
# def get_all_categories():
#     c = ModelRepositories(model_type=Category)
#     the_categories = c.get_all()
#     if the_categories is None:
#         return JSONResponse(**fomatter.error_get_by_id_response('category'))
#     return JSONResponse(**fomatter.success_get_all_response(the_categories))

# @category_router.delete('')
# def delete_category_by_id(id:int):
#     c = ModelRepositories(model_type=Category)
#     the_category = c.get_by_id(id=id)
#     if the_category is None:
#         return JSONResponse(**fomatter.error_get_by_id_response('category',id))
#     c.delete_object(the_category)
#     return JSONResponse(**fomatter.success_delete_response('category',id))

# @category_router.put('')
# def update_category_by_id(category:CategoryUpdate = Depends(),image:UploadFile | None = None ):
#     c = ModelRepositories(model_type=Category)
#     the_category = c.get_by_id(id=category.id)
#     if the_category is None:
#         return JSONResponse(**fomatter.error_get_by_id_response('category',id))
#     if image:
#         image_path = c.file_upload_and_save(image,'category')
#         category = category.dict()
#         category['image'] = image_path

#     the_category = c.update_object(the_category,data=category)
#     return JSONResponse(**fomatter.success_update_response(the_category,'category',id))

# category APIs ends

# product APIs start here
@product_router.post('')
def create_product(product:ProductCreate):
    c = ModelRepositories(model_type=Product)
    the_product = c.create(product)
    print(the_product)
    return JSONResponse(**fomatter.success_post_response('product',the_product))

@product_router.get('')
def get_product_by_id(id:int):
    c = ModelRepositories(model_type=Product)
    the_product = c.get_by_id(id=id)
    if the_product is None:
        return JSONResponse(**fomatter.error_get_by_id_response('product',id))
    return JSONResponse(**fomatter.success_get_response(the_product,ProductModel))


@product_router.get('/all')
def get_all_products():
    c = ModelRepositories(model_type=Product)
    the_products = c.get_all()
    if the_products is None:
        return JSONResponse(**fomatter.error_get_by_id_response('product'))
    return JSONResponse(**fomatter.success_get_all_response(the_products))

@product_router.delete('')
def delete_product_by_id(id:int):
    c = ModelRepositories(model_type=Product)
    the_product = c.get_by_id(id=id)
    if the_product is None:
        return JSONResponse(**fomatter.error_get_by_id_response('product',id))
    c.delete_object(the_product)
    return JSONResponse(**fomatter.success_delete_response('product',id))

@product_router.put('')
def update_prodct_by_id(id:int,product:ProductCreate):
    c = ModelRepositories(model_type=Product)
    the_product = c.get_by_id(id=id)
    if the_product is None:
        return JSONResponse(**fomatter.error_get_by_id_response('product',id))
    the_product = c.update_object(the_product,data=product)
    return JSONResponse(**fomatter.success_update_response(the_product,'product',id))

# product_images API

@product_image_router.post('')
def create_product_image(product_image:ProductImageCreate=Depends(),image:UploadFile | None = None):
    c = ModelRepositories(model_type=ProductImage)
    image_path = c.file_upload_and_save(image,'product')
    product_image = product_image.dict()
    product_image['image_url'] = image_path
    the_product_image = c.create(product_image)
    return JSONResponse(**fomatter.success_post_response('product_image',the_product_image))

@product_image_router.get('')
def get_product_image_by_id(id:int):
    c = ModelRepositories(model_type=ProductImage)
    the_product_image = c.get_by_id(id=id)
    if the_product_image is None:
        return JSONResponse(**fomatter.error_get_by_id_response('product_image',id))
    return JSONResponse(**fomatter.success_get_response(the_product_image,ProductImageModel))


@product_image_router.get('/all')
def get_all_product_images():
    c = ModelRepositories(model_type=ProductImage)
    the_product_images = c.get_all()
    if the_product_images is None:
        return JSONResponse(**fomatter.error_get_by_id_response('product_image'))
    return JSONResponse(**fomatter.success_get_all_response(the_product_images))

@product_image_router.delete('')
def delete_product_image_by_id(id:int):
    c = ModelRepositories(model_type=ProductImage)
    the_product_image = c.get_by_id(id=id)
    if the_product_image is None:
        return JSONResponse(**fomatter.error_get_by_id_response('product_image',id))
    c.delete_object(the_product_image)
    return JSONResponse(**fomatter.success_delete_response('product_image',id))

@product_image_router.put('')
def update_product_image_by_id(product_image:ProductImageUpdate = Depends(),image:UploadFile | None = None):
    c = ModelRepositories(model_type=ProductImage)
    the_product_image = c.get_by_id(id=id)
    if the_product_image is None:
        return JSONResponse(**fomatter.error_get_by_id_response('product_image',id))
    if image:
        image_path = c.file_upload_and_save(image,'product')
        product_image = product_image.dict()
        product_image['image_url'] = image_path
    the_product_image = c.update_object(the_product_image,data=product_image)
    return JSONResponse(**fomatter.success_update_response(the_product_image,'product_image',id))








