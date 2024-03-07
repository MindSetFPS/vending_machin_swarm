from Server.Models.VendingMachine import VendingMachine
from Server.Repository.Repository import IDatabase
from Server.Repository.VendingMachineRepository import vending_machine_repository


class VendingMachineController:
    def __init__(self, vending_machine_repository: IDatabase) -> None:
        self.repository = vending_machine_repository

    def create_vendingmachine(self):
        print("Creating vending machine")
        vending_machine = VendingMachine()
        self.repository.create(vending_machine)


vending_machine_controller = VendingMachineController(vending_machine_repository=vending_machine_repository)