# from Repository.Repository import IDatabase, repository
from Server.Repository.Repository import IDatabase, repository
from sqlmodel import select
from Server.Models.Sale import Sale
from Server.Models.Product import Product

class SaleRepository:
    def __init__(self, repository: IDatabase) -> None:
        self._repository = repository

    def get_all(self):
        statement = select(Sale)
        return self._repository.get_all(statement)
    
    def get_by_id(self, id: int):
        statement = select(Sale).where(Sale.id == id)
        return self._repository.get_by_id(statement)

    def delete(self, id):
        return self._repository.delete(id)

    def create(self, sale):
        return self._repository.create(sale)    
    
    def update(self, id):
        return self._repository.update(id)
    
    def get_sales_by_machine_id(self, machine_id:int):
        statement = select(Sale, Product).join(Product).where(Sale.machine_id == machine_id)
        return self._repository.get_all(statement=statement)
    
sale_repository = SaleRepository(repository=repository)