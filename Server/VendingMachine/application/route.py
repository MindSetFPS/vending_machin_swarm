from fastapi import APIRouter

from .VendingMachineController import vending_machine_controller
from .VendingMachineProductStockController import vending_machine_product_stock_controller, VendingMachineProductsLink
from Server.Incident.application.IncidentController import incident_controller
from Server.Incident.domain.Incident import Incident, Status

from Server.VendingMachine.domain.VendingMachine import VendingMachine

from typing import List

router = APIRouter(
    prefix="/api/vendingmachine",
    tags=["vending machines"]
)

# Listar todas maquinas
@router.get("/api/vendingmachine/all")
async def get_all_vending_machines():
    print('/api/vendingmachine/all')
    v = vending_machine_controller.get_all()
    print(v)
    return v

# Listar una maquina
@router.get("/api/vendingmachine/{id}")
async def get_machine(machine_id: int):
    
    vending_machine = vending_machine_controller.get_vending_machine_by_id(id=machine_id)
    print(vending_machine)
    if vending_machine is None:
        return {
            "result" : "Vending Machine not found."
        }

    return {
        'machine' : vending_machine
    }

# Obtener los productos de una maquina
@router.get("/api/vendingmachine/{machine_id}/products")
async def get_products_by_vending_machine(machine_id: int):
    vending_machine = vending_machine_controller.get_vending_machine_by_id(id=machine_id)

    if not vending_machine:
        return {
            "error" : "No such vending machine"
        }
    
    vending_machine_products_list = vending_machine_product_stock_controller.get_products_by_machine_id(machine_id=machine_id)
    return vending_machine_products_list

# Modificar una maquina
@router.post("/api/vendingmachine/update")
async def update_vending_machine(id: int, is_on: bool):
    vending_machine_controller.update_vending_machine(id=id, is_on=is_on)
    return {
        'machine' : 'true'
    }

# Rellenar una maquina
@router.post("/api/vendingmachine/refill")
async def refill_vending_machine(vending_machine_stock: VendingMachineProductsLink):
        print(type(vending_machine_stock.stock))
        vending_machine_product_stock_controller.refill_vending_machine(machine_id=vending_machine_stock.machine_id, product_id=vending_machine_stock.product_id, stock=int(vending_machine_stock.stock))

# Asignar productos a una maquina
@router.post("/api/vendingmachine/assign/{machine_id}")
async def assign_products_to_vending_machine(products: List[int], machine_id: int):
    for product_id in products:
        vending_machine_product_stock_controller.refill_vending_machine(machine_id=machine_id, product_id=product_id, stock=0)
        incident_controller.create_incident(incident=Incident(description=Status.refill_required, active=True, product_id=product_id, machine_id=machine_id))
    
    return {
        "ok": True
    }

# Crear una maquina (en el servidor)
@router.post("/api/vendingmachine/create")
async def create_vending_machine(vendingMachine: VendingMachine):
    vending_machine_controller.create_vendingmachine(vendingMachine)
    return {
        "ok": "True"
    }

# Borrar una maquina
@router.delete("/api/vendingmachine/delete/{id}")
async def delete_vending_machine(id: int):
    vending_machine_controller.delete_vending_machine(id=id)
    return {
        "we": "did_something"
    }

# Mostrar maquina con mas ventas
@router.get("/api/vendingmachines/top_selling")
async def get_top_selling_machines():
    top_selling_machines = vending_machine_controller.get_top_selling_machines()
    return top_selling_machines

