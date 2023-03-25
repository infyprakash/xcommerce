from fastapi import HTTPException,status
from src.core.container import Container
from src.catalogue.models import Category
from fastapi.responses import JSONResponse


class CatalogueRepositories:
    def __init__(self,model_type):
        self._session = Container().db_obj().get_session()
        self._model_type = model_type
    def create(self,kwargs):
        try:
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
        hero_data = data.dict(exclude_unset=True)
        for key, value in hero_data.items():
            setattr(obj, key, value)
        self._session.add(obj)
        self._session.commit()
        self._session.refresh(obj)
        return obj

            


