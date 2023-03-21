from dependency_injector import containers,providers
from src.db.database import Database
from src.core.config import setting

class Container(containers.DeclarativeContainer):
    db_obj = providers.Singleton(Database,db_url=setting.DATABASE_URL)
    
