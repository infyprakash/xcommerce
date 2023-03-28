import os,shutil
import logging

from datetime import datetime
from fastapi import HTTPException,status
from src.core.container import Container
from src.catalogue.models import Category
from fastapi.responses import JSONResponse
from src.core.config import setting

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class ModelRepositories(object):
    def __init__(self,model_type):
        self._session = Container().db_obj().get_session()
        self._model_type = model_type
    def create(self,kwargs):
        try:
            if type(kwargs) == dict:
                the_ob = self._model_type(**kwargs)
            else:
                the_ob = self._model_type(**kwargs.dict())
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,detail=str(e))
        else:
            self._session.add(the_ob)
            self._session.commit()
            self._session.refresh(the_ob)
        return the_ob
    def get_by_id(self,id):
        the_ob = self._session.query(self._model_type).filter_by(id=id,is_active=True).first()
        return the_ob
    
    def get_all(self):
        the_ob =  self._session.query(self._model_type).filter_by(is_active=True).all()
        return the_ob
    
    def delete_object(self, obj):
        obj.is_active = False
        self._session.add(obj)
        self._session.commit()
    
    def update_object(self,obj,data):
        if type(data)==dict:
            hero_data = data(exclude_unset=True)
        else:
            hero_data = data.dict(exclude_unset=True)
        for key, value in hero_data.items():
            setattr(obj, key, value)
        self._session.add(obj)
        self._session.commit()
        self._session.refresh(obj)
        return obj

    def file_upload_and_save(self,file_obj,module_name):
        media_path = ModelRepositories.create_upload_directory(module_name)
        file_name = None 
        try:
            image_path = media_path +file_obj.filename
            if ModelRepositories.check_extension(image_path=image_path):
                with open(image_path,"wb") as buffer:
                    shutil.copyfileobj(file_obj.file, buffer)
                logging.info(f'      [X] file saved to {media_path}')
                file_name = file_obj.filename
            else:
                raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,detail=f'{file_obj.filename} not supported')
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,detail=str(e))
        finally:
            file_name = media_path +file_obj.filename
            file_obj.file.close()
    
        return file_name
        

    @staticmethod
    def create_upload_directory(module_name:str):
        now = datetime.now().strftime('%Y/%m/%d/')
        media_dir = os.path.join('static',module_name,now)
        if not os.path.exists(media_dir):
            os.makedirs(media_dir)
        return media_dir
    @staticmethod
    def check_extension(image_path:str):
        if not image_path.endswith(setting.IMAGE_ALLOWED_EXTENSION):
            return False
        else:
            return True

            


