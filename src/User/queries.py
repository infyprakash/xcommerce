from src.core.repositories import ModelRepositories 
from fastapi import HTTPException,status

class UserRepositories(ModelRepositories):
    def __init__(self, model_type):
        super().__init__(model_type)
    def check_user_exists(self,username):
        the_ob = self._session.query(self._model_type).filter_by(phone_no=username,is_active=True).first()
        return the_ob
    def get_user_by_id(self,id:int):
        the_ob = self._session.query(self._model_type).filter_by(id=id,is_active=True).first()
        return the_ob    
