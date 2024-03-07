from Server.Repository.Repository import IDatabase, repository

class VendingMachineRepository:
    def __init__(self, repository: IDatabase) -> None:
        self._repository = repository

    def get_all_items(self):
        return self._repository.get_all("SELECT * FROM products")
    
    def get_by_id(self, id):
        return self._repository.get_by_id(id)
    
    def delete(self, id):
        return self._repository.delete(id)
    
    def create(self, vending_machine):
        return self._repository.create(vending_machine)
    
    def update(self, id):
        return self._repository.update(id)
    
vending_machine_repository = VendingMachineRepository(repository=repository)