from Server.Models.Sale import Sale
from Server.Models.Incident import Incident

from Server.Repository.Repository import IDatabase
from Server.Repository.SaleRepository import sale_repository
from Server.Controllers.IncidentController import incident_controller
from Server.Controllers.VendingMachineProductStockController import vending_machine_product_stock_controller
from Server.Models.Incident import Status

class SaleController:
    def __init__(self, sale_repository: IDatabase) -> None:
        self.sale_repository = sale_repository

    def create_sale(self, product_id: int, machine_id: 1):
        # Check if we have stock

        v = vending_machine_product_stock_controller.get_by_id(machine_id=machine_id, product_id=product_id)
        print('v')
        print(v)

        if v is not None and v.stock > 0:
            if v.stock == 1:
                incident = Incident(
                    description=Status.refill_required,
                    fix_at_url=f"/machines/{machine_id}",
                    active=True,
                    machine_id=machine_id,
                    product_id=product_id
                )
                incident_controller.create_incident(incident)
            sale = Sale(product_id=product_id, machine_id=machine_id)
            self.sale_repository.create(sale=sale)

            vending_machine_product_stock_controller.decrease_product_stock(
                machine_id=machine_id, 
                product_id=product_id,
            )
            return True
        else:   
            return False
        
    def get_sale_by_id(self, sale_id: int):
        sale = self.sale_repository.get_by_id(id=sale_id)
        return sale
    
    def get_sales(self):
        sales = self.sale_repository.get_all()
        return sales
    
    def get_sales_by_machine_id(self, machine_id: int):
        sales = self.sale_repository.get_sales_by_machine_id(machine_id=machine_id)
        return sales

sale_controller = SaleController(sale_repository=sale_repository)