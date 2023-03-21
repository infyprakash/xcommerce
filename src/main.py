from fastapi import FastAPI 
from src.core.config import setting
from src.core.container import Container


def include_routes(app):
    from src.catalogue.routes import router as catalog_router
    app.include_router(catalog_router)

def start_application():
    app = FastAPI(title=setting.PROJECT_NAME,version=setting.PROJECT_VRESION)
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

  
