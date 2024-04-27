from Server.Repository.Repository import IDatabase, repository
from Server.VendingMachine.domain.VendingMachine import VendingMachine, VendingMachineProductsLink
from sqlmodel import select

class VendingMachineRepository:
    def __init__(self, repository: IDatabase) -> None:
        self._repository = repository

    def get_all(self, statement):
        return self._repository.get_all(statement)
    
    def get_by_id(self, id):
        statement = select(VendingMachine).where(VendingMachine.id == id)
        return self._repository.get_by_id(statement)
    
    def delete(self, id):
        vending_machine = self.get_by_id(id=id)
        return self._repository.delete(vending_machine)
    
    def create(self, vending_machine):
        return self._repository.create(vending_machine)
    
    def update(self, id):
        return self._repository.update(id)
    
vending_machine_repository = VendingMachineRepository(repository=repository)