from abc import ABC, abstractmethod

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

class IDatabase(ABC):
    @abstractmethod
    def connect(self):
        raise NotImplementedError

    @abstractmethod
    def disconnect(self):
        raise NotImplementedError

    @abstractmethod
    def get_all(self, query):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, query):
        raise NotImplementedError
    
    @abstractmethod
    def create(self, item):
        raise NotImplementedError
    
    @abstractmethod
    def update(self, item):
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, item):
        raise NotImplementedError
    
class SQLiteRepository(IDatabase):
    def __init__(self, db_path: str) -> None:
        super().__init__()

        self.db_path = db_path
        self.connect()
    
    def connect(self):
        engine = create_engine("sqlite:///{0}".format(self.db_path), echo=True)
        Base = declarative_base()

        class User(Base):
            __tablename__ = "users"
            id = Column(Integer, primary_key=True)
            name = Column(String)
            email = Column(String)

        Base.metadata.create_all(engine)
    
    def disconnect(self):
        pass
    
    def get_all(self, query):
        pass
    def get_by_id(self, query):
        pass

    def create(self, item):
        pass

    def update(self, item):
        pass

    def delete(self, item):
        pass