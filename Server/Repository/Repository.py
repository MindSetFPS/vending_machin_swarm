from abc import ABC, abstractmethod

from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from sqlmodel import create_engine, SQLModel, Session

from Server.Repository.SQLBase import Base

# We need to have these classes here to register them in database
from Server.Models.Dinero import Dinero
from Server.Models.Product import Product
from Server.Models.Sale import Sale
from Server.Models.VendingMachine import VendingMachine

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
        # self.connection = self.engine.connect()
        SQLModel.metadata.create_all(self.engine)

        # Base.metadata.create_all(self.engine)
    
    def disconnect(self):
        pass
    
    def get_all(self, query):
        sql = text(query)
        return self.connection.execute(sql)

    def get_by_id(self, query): 
        pass
    
    def show_product(self, product_id):
    with Session(self.engine) as session:
        product = session.query(Product).filter_by(id=product_id).first()

    def create(self, product):
        session = Session(self.engine)
        session.add(product)

        session.commit()

    def update(self, item):
         with Session(self.engine) as session:
            session.merge(item)
            session.commit()

    def delete(self, item):
        with Session(self.engine) as session:
            
            session.delete(item)
            session.commit()

repository = SQLiteRepository(db_path="database.db")
repository.connect()