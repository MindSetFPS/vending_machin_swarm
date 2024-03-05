# from Repository.ProductRepository import product_repository
from Server.Repository.ProductRepository import product_repository
# from Repository.Repository import IDatabase
from Server.Repository.Repository import IDatabase
from Server.Models.Product import Product

class ProductController:
    def __init__(self, product_repository: IDatabase ) -> None:
        self.product_repository = product_repository
    
    def getProductById(self, id: int):
        self.product_repository.get_by_id(id=id)

    def createProduct(self, name: str, price: float, code: str):
        product = Product(name=name, price=price, code=code)
        print(product)
        self.product_repository.create(product)
    
    def Delete_Product(self, id):
        self.product_repository.delete_by_id(id=id)

    

product_controller = ProductController(product_repository=product_repository)