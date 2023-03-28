import os,shutil
import logging

from datetime import datetime
from fastapi import HTTPException,status
from src.core.container import Container
from src.catalogue.models import Category
from fastapi.responses import JSONResponse
from src.core.repositories import ModelRepositories
from src.core.config import setting

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)



class CatalogueRepositories(ModelRepositories):
    def __init__(self, model_type):
        super().__init__(model_type) 
    def file_upload_and_save(self,file_obj):
        media_path = CatalogueRepositories.create_upload_directory()
        file_name = None 
        try:
            image_path = media_path +file_obj.filename
            if CatalogueRepositories.check_extension(image_path=image_path):
                with open(image_path,"wb") as buffer:
                    shutil.copyfileobj(file_obj.file, buffer)
                logging.info(f'      [X] file saved to {media_path}')
                file_name = file_obj.filename
            else:
                raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,detail=f'{file_obj.filename} not supported')
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,detail=str(e))
        finally:
            file_obj.file.close()
    
        return file_obj.filename
        

    @staticmethod
    def create_upload_directory():
        now = datetime.now().strftime('%d/%m/%Y/')
        media_dir = os.path.join(setting.MEDIA_DIR,now)
        if not os.path.exists(media_dir):
            os.makedirs(media_dir)
        return media_dir
    @staticmethod
    def check_extension(image_path:str):
        if not image_path.endswith(setting.IMAGE_ALLOWED_EXTENSION):
            return False
        else:
            return True

            





