import os 
from fastapi import FastAPI 
from src.core.config import setting
from src.core.container import Container
from fastapi.staticfiles import StaticFiles



def include_routes(app):
    # from src.catalogue.routes import category_router
    from src.catalogue.routes import product_router
    from src.catalogue.routes import product_image_router
    from src.user.routes import user_router
    from src.showroom.routes import shop_router,address_router,shop_category_router

    # app.include_router(category_router)
    app.include_router(product_router)
    app.include_router(product_image_router)
    app.include_router(user_router)
    app.include_router(address_router)
    app.include_router(shop_router)
    app.include_router(shop_category_router)

def start_application():
    app = FastAPI(title=setting.PROJECT_NAME,version=setting.PROJECT_VRESION)
    app.mount("/static", StaticFiles(directory="static"), name="static")
    container = Container().db_obj()
    include_routes(app)
    return container,app 

container,app = start_application()

@app.on_event('startup')
async def startup():
    container.create_database()

@app.on_event('shutdown')
async def shutdown():
    container.destroy_session()




  
