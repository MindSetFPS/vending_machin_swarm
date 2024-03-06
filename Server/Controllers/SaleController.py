from Server.Models.Sale import Sale
from Server.Repository.Repository import IDatabase
from Server.Repository.SaleRepository import sale_repository

class SaleController:
    def __init__(self, sale_repository: IDatabase) -> None:
        self.sale_repository = sale_repository

    def create_sale(self, product_id: int):
        sale = Sale(product_id=product_id)
        self.sale_repository.create(sale=sale)

sale_controller = SaleController(sale_repository=sale_repository)