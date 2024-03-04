from abc import ABC, abstractmethod

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from SQLBase import Base

# We need to have these classes here to register them in database
from Dinero import Dinero
from Producto import Producto

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
        self.engine = create_engine("sqlite:///{0}".format(self.db_path), echo=True)
        self.connection = self.engine.connect()

        Base.metadata.create_all(self.engine)
    
    def disconnect(self):
        pass
    
    def get_all(self, query):
        sql = text(query)
        return self.connection.execute(sql)
        

    def get_by_id(self, query): 
        pass

    def create(self, item):
        pass

    def update(self, item):
        pass

    def delete(self, item):
        pass