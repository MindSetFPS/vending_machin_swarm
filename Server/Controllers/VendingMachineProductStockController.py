from Server.Repository.Repository import IDatabase
from Server.Repository.VendingMachineProductStockRepository import vending_machine_product_stock_repository
from Server.Models.VendingMachine import VendingMachineProductsLink
from sqlmodel import select

class VendingMachineProductStockLinkController:
    def __init__(self, vending_machine_product_stock_link_repository: IDatabase ) -> None:
        self.repository = vending_machine_product_stock_link_repository

    def get_all(self, statement):
        return self.repository.get_all(query=statement)

    def get_by_id(self, machine_id: int, product_id: int):
        return self.repository.get_by_id(machine_id=machine_id, product_id=product_id)
    
    def refill_vending_machine(self, machine_id, product_id, stock):
        table = self.repository.get_by_id(machine_id=machine_id, product_id=product_id)
        
        if table is None:
            new_refill = VendingMachineProductsLink(machine_id=machine_id, product_id=product_id, stock=stock)
            print("Creating")
            self.repository.create(new_refill)
        
        if table is not None:
            print("Updating")
            table.stock = table.stock + stock
            self.repository.update(table)

    def decrease_product_stock(self, machine_id, product_id):
        stock = self.repository.get_by_id(machine_id=machine_id, product_id=product_id)
        stock.stock = stock.stock -10

        self.repository.update(stock)

vending_machine_product_stock_controller = VendingMachineProductStockLinkController(
    vending_machine_product_stock_link_repository=vending_machine_product_stock_repository
)