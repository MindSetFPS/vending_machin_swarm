from Server.Models.Sale import Sale

from Server.Repository.Repository import IDatabase
from Server.Repository.SaleRepository import sale_repository

from Server.Controllers.VendingMachineProductStockController import vending_machine_product_stock_controller

class SaleController:
    def __init__(self, sale_repository: IDatabase) -> None:
        self.sale_repository = sale_repository

    def create_sale(self, product_id: int, machine_id: 1):
        # Check if we have stock

        v = vending_machine_product_stock_controller.get_by_id(machine_id=machine_id, product_id=product_id)
        print('v')
        print(v)

        if v.stock <= 0:
            return False
        else:   
            sale = Sale(product_id=product_id, machine_id=machine_id)
            self.sale_repository.create(sale=sale)

            vending_machine_product_stock_controller.decrease_product_stock(
                machine_id=machine_id, 
                product_id=product_id,
            )

            return True

sale_controller = SaleController(sale_repository=sale_repository)