from abc import ABC, abstractmethod
from sqlmodel import create_engine, SQLModel, Session

# We need to have these classes here to register them in database
from Server.Models.Dinero import Dinero
from Server.Models.Product import Product
from Server.Sale.domain.Sale import Sale
from Server.VendingMachine.domain.VendingMachine import VendingMachine, VendingMachineProductsLink
from Server.Incident.domain.Incident import Incident

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
        SQLModel.metadata.create_all(self.engine)
    
    def disconnect(self):
        pass
    
    def get_all(self, statement):
        session = Session(self.engine)
        with session:
            results = session.exec(statement).all()
        return results

    def get_by_id(self, query): 
        session = Session(self.engine)
        with session:
            results = session.exec(statement=query).one_or_none()
        return results

    def create(self, model):
        session = Session(self.engine)
        session.add(model)

        session.commit()

    def update(self, item):
         with Session(self.engine) as session:
            session.add(item)
            session.merge(item)
            session.commit()

    def delete(self, item):
        with Session(self.engine) as session:
            session.delete(item)
            session.commit()

repository = SQLiteRepository(db_path="database.db")
# repository.connect()