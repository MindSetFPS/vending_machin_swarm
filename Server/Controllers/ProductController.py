# from Repository.ProductRepository import product_repository
from Server.Repository.ProductRepository import product_repository
# from Repository.Repository import IDatabase
from Server.Repository.Repository import IDatabase
from Server.Models.Product import Product
from sqlmodel import select

class ProductController:
    def __init__(self, product_repository: IDatabase ) -> None:
        self.product_repository = product_repository

    def get_all_products(self):
        statement = select(Product)
        return self.product_repository.get_all(statement)
    
    def getProductById(self, id: int):
        self.product_repository.get_by_id(id=id)

    def createProduct(self, name: str, price: float, code: str):
        product = Product(name=name, price=price, code=code)
        print(product)
        self.product_repository.create(product)
    
    def Delete_Product(self, id):
        self.product_repository.delete_by_id(id=id)
        
    #modificar un producto
    def update_product(self, id: int, updated_product_data: dict):
        self.product_repository.get_by_id(id)

    

product_controller = ProductController(product_repository=product_repository)