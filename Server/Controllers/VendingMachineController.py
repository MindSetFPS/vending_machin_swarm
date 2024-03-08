from Server.Models.VendingMachine import VendingMachine, VendingMachineProductsLink
from Server.Repository.Repository import IDatabase
from Server.Repository.VendingMachineRepository import vending_machine_repository
from Server.Controllers.VendingMachineProductStockController import vending_machine_product_stock_controller
from sqlmodel import select

class VendingMachineController:
    def __init__(self, vending_machine_repository: IDatabase) -> None:
        self.repository = vending_machine_repository

    def create_vendingmachine(self, vending_machine: VendingMachine = None,  is_on: bool = None):
        print("Creating vending machine")
        if vending_machine is not None:
            db_query = self.get_vending_machine_by_id(id=vending_machine.id)
            
            if db_query is not None:
                return db_query
            else:
                self.repository.create(vending_machine)
        else:
            vending_machine = VendingMachine(is_on=is_on)
            self.repository.create(vending_machine)
        return vending_machine
    
    def update_vending_machine(self, id: int, is_on: bool):
        machine = self.get_vending_machine_by_id(id=id)
        machine.is_on = bool(is_on)
        self.repository.update(machine)
    
    def get_vending_machine_by_id(self, id: int):
        return self.repository.get_by_id(id=id)

    def delete_vending_machine(self, id):
        print(f'Deleting vending machine with id {id}')
        self.repository.delete(id=id)

    def get_top_selling_machines(self):
        machines = select(VendingMachineProductsLink).group_by(VendingMachineProductsLink.machine_id)
        machines_group = vending_machine_product_stock_controller.get_all(machines)
        print(machines_group)

vending_machine_controller = VendingMachineController(vending_machine_repository=vending_machine_repository)