import os 
from dotenv import load_dotenv
from fastapi import status
from fastapi.encoders import jsonable_encoder


from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

CURRENT_DIR = Path( os.path.dirname(os.path.abspath(__file__)))

class Settings:
    PROJECT_NAME:str = "intelligent ecommerce application"
    PROJECT_VRESION:str = "0.0.0"
    SRC_DIR = CURRENT_DIR.parent.absolute()
    MEDIA_DIR = Path('.') / 'media'
    IMAGE_ALLOWED_EXTENSION = ('.png','jpg','.jpeg')


    POSTGRES_USER:str = os.getenv('POSTGRES_USER','prakash')
    POSTGRES_PASSWORD:str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_SERVER:str = os.getenv('POSTGRES_SERVER')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT',5432)
    POSTGRES_DB= os.getenv('POSTGRES_DB','xdb')
    DATABASE_URL:str = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}'

    #authentication
    ACCESS_TOKEN_EXPIRE_MINUTES:str = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
    REFRESH_TOKEN_EXPIRE_MINUTES:str = os.getenv('REFRESH_TOKEN_EXPIRE_MINUTES')
    ALGORITHM:str = os.getenv('ALGORITHM',"HS256")
    JWT_SECRET_KEY:str = os.getenv('JWT_SECRET_KEY')
    JWT_REFRESH_SECRET_KEY:str = os.getenv('JWT_REFRESH_SECRET_KEY')

    

class DataFormatter:
    @staticmethod
    def success_post_response(model_name,data):
        content = {
            'content':{
            'message': f'{model_name} successfully created',
            'data': jsonable_encoder(data),
            'status_code': status.HTTP_200_OK
            },
            'status_code': status.HTTP_201_CREATED
        }
        return content
    
    @staticmethod
    def success_get_response(data,schema):
        content = {
            'content':{
            'message': 'success',
            'data': jsonable_encoder(schema.from_orm(data)),
            'status_code': status.HTTP_200_OK
            },
            'status_code': status.HTTP_200_OK
        }
        return content

    @staticmethod
    def success_get_all_response(data):
        content = {
            'content':{
            'message': 'success',
            'data': jsonable_encoder(data),
            'status_code': status.HTTP_200_OK
            },
            'status_code': status.HTTP_200_OK
        }
        return content
    
    @staticmethod
    def error_get_by_id_response(model_name,id):
        content = {
            'content':{
            'message': f'{model_name} with id = {id} not found',
            'data': None,
            'status_code': status.HTTP_404_NOT_FOUND
            },
            'status_code': status.HTTP_404_NOT_FOUND
        }
        return content
    
    
    @staticmethod
    def error_get_response(model_name):
        content = {
            'content':{
            'message': f'No enteries found for {model_name}',
            'data': None,
            'status_code': status.HTTP_404_NOT_FOUND
            },
            'status_code': status.HTTP_404_NOT_FOUND
        }
        return content
    
    @staticmethod
    def success_delete_response(model_name,id):
        content = {
            'content':{
            'message': f'{model_name} with id = {id} successfully deleted',
            'data': None,
            'status_code': status.HTTP_200_OK
            },
            'status_code': status.HTTP_200_OK
        }
        return content

    @staticmethod
    def success_update_response(data,model_name,id):
        content = {
            'content':{
            'message': f'{model_name} with id = {id} successfully updated',
            'data': jsonable_encoder(data),
            'status_code': status.HTTP_200_OK
            },
            'status_code': status.HTTP_200_OK
        }
        return content



setting = Settings()
fomatter = DataFormatter()