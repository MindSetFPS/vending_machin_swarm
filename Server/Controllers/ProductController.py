from Repository.ProductRepository import product_repository
from Repository.Repository import IDatabase

class ProductController:
    def __init__(self, product_repository: IDatabase ) -> None:
        self.product_repository = product_repository
    
    def getProductById(self, id: int):
        self.product_repository.get_by_id(id=id)

product_controller = ProductController(product_repository=product_repository)