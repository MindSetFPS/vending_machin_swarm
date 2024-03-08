from Server.Repository.Repository import IDatabase, repository
from Server.Models.VendingMachine import VendingMachine, VendingMachineProductsLink
from sqlmodel import select

class VendingMachineProductStockRepository:
    def __init__(self, repository: IDatabase) -> None:
        self._repository = repository

    def get_by_id(self, machine_id, product_id) -> VendingMachineProductsLink:
        statement = select(VendingMachineProductsLink).where(
            VendingMachineProductsLink.machine_id == machine_id and VendingMachineProductsLink.product_id == product_id
        )
        return self._repository.get_by_id(statement)
    
    def update(self, statement):
        repository.update(item=statement)

    def get_all(self, query):
        return repository.get_all(statement=query)
    
    def create(self, statement):
        repository.create(statement)    

vending_machine_product_stock_repository = VendingMachineProductStockRepository(repository=repository)