# from Repository.Repository import IDatabase, repository
from Server.Repository.Repository import IDatabase, repository
from sqlmodel import select
from Server.Models.Product import Product

class ProductRepository:
    def __init__(self, repository: IDatabase) -> None:
        self._repository = repository
    
    def get_all(self, statement):
        return self._repository.get_all(statement)
    
    def get_by_id(self, id):
        statement = select(Product).where(Product.id == id)
        return self._repository.get_by_id(statement)
    
    def delete(self, id):
        return self._repository.delete(id)
    
    def create(self, product):
        return self._repository.create(product)
    
    def update(self, id):
        return self._repository.update(id)
    
product_repository = ProductRepository(repository=repository)
