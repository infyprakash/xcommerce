import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,scoped_session,Session
from sqlalchemy import Column,Boolean,Integer,String,Float,Unicode,DateTime,ForeignKey
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship
from sqlalchemy.pool import StaticPool
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from uuid import uuid4



logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

Base = declarative_base()


class Database:
    def __init__(self,db_url:str) -> None:
        logger.info(f'[X]       Connecting to database: {db_url}')
        try:
            self.db_url = db_url
            self._engine = create_engine(db_url,poolclass=StaticPool,echo=False)
        except Exception as e:
            self._engine.dispose()
            self._session_factory.remove()
        else:
            self._session_maker = sessionmaker(autocommit=False,autoflush=False,future=True,bind=self._engine)
            self._session_factory = scoped_session(self._session_maker)
        finally:
            self._engine.dispose()
            self._session_factory.remove()



    def models_import(self):
        from src.catalogue import models

    def create_database(self)->None:
        try:
            self.models_import()
            Base.metadata.create_all(bind=self._engine)
            Base.query = self._session_factory.query_property()
        except Exception as e:
            logger.error(e)

        

    def get_session(self)->Session:
        session:Session = self._session_factory
        try:
            return session
        except Exception as e:
            logger.exception('[X]       session roll back because of exception')
            session.rollback()
            raise 
        finally:
            session.close()
            
    def destroy_session(self):
        logger.info(f'[X]       Disconnecting from database: {self.db_url}')
        self._engine.dispose()
        # self._session_maker.close_all()
        self._session_factory.remove()


