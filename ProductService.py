from Repository import IDatabase

class ProductService:
    def __init__(self, repository: IDatabase) -> None:
        self._repository = repository
    
    def get_all_items(self):
        return self._repository.get_all("SELECT * FROM products")
    
    def get_by_id(self, id):
        return self._repository.get_by_id(id)
    
    def delete(self, id):
        return self._repository.delete(id)
    
    def create(self):
        return self._repository.create()
    
    def update(self, id):
        return self._repository.update(id)