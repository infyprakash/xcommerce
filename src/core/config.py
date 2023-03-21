import os 
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME:str = "intelligent ecommerce application"
    PROJECT_VRESION:str = "0.0.0"

    POSTGRES_USER:str = os.getenv('POSTGRES_USER','prakash')
    POSTGRES_PASSWORD:str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_SERVER:str = os.getenv('POSTGRES_SERVER')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT',5432)
    POSTGRES_DB= os.getenv('POSTGRES_DB','xdb')
    DATABASE_URL:str = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}'

setting = Settings()
