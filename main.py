from Server.Repository.ProductRepository import product_repository

from Server.Controllers.ProductController import product_controller
from Server.Controllers.SaleController import sale_controller 
from Server.Controllers.VendingMachineController import vending_machine_controller
from Server.Controllers.VendingMachineProductStockController import vending_machine_product_stock_controller

from Server.Models.Product import Product
from Server.Models.VendingMachine import VendingMachine, VendingMachineProductsLink
from Server.Models.Sale import Sale

from fastapi import FastAPI, Request
from typing import Optional
import json

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message" : "Hello World"
    }

# Listar todas maquinas
@app.get("/api/vendingmachine/all")
async def get_all_vending_machines():
    print('/api/vendingmachine/all')
    v = vending_machine_controller.get_all()
    print(v)
    return v

# Modificar una maquina
@app.post("/api/vendingmachine/update")
async def update_vending_machine(id: int, is_on: bool):
    vending_machine_controller.update_vending_machine(id=id, is_on=is_on)
    return {
        'machine' : 'true'
    }

@app.post("/api/vendingmachine/refill")
async def refill_vending_machine(product_id: int, machine_id: int, stock: int):
        vending_machine_product_stock_controller.refill_vending_machine(machine_id=machine_id, product_id=product_id, stock=stock)
        # vending_machine_controller.refill_vending_machine(product_id, machine_id, stock)

# Listar una maquina
@app.get("/api/vendingmachine")
async def get_machine(machine: Request):
    
    machine_json = await machine.json()
    vending_machine = vending_machine_controller.get_vending_machine_by_id(id=machine_json['id'])
    print(vending_machine)
    if vending_machine is None:
        vending_machine_controller.create_vendingmachine(is_on=machine_json['is_on'])

        vending_machine = vending_machine_controller.get_vending_machine_by_id(id=machine_json['id'])

    return {
        'machine' : vending_machine
    }

# Borrar una maquina
@app.delete("/api/vendingmachine/delete/{id}")
async def delete_vending_machine(id: int):
    vending_machine_controller.delete_vending_machine(id=id)
    return {
        "we": "did_something"
    }

# Crear una maquina (en el servidor)
@app.post("/api/vendingmachine/create")
async def create_vending_machine(vendingMachine: VendingMachine):
    vending_machine_controller.create_vendingmachine(vendingMachine)
    return {
        "ok": "True"
    }

# Mostrar maquina con mas ventas
@app.get("/api/vendingmachines/top_selling")
async def get_top_selling_machines():
    top_selling_machines = vending_machine_controller.get_top_selling_machines()
    return top_selling_machines

#################################################

# Listar todos los productos
@app.get("/api/products")
async def get_all_products():
    products = product_controller.get_all_products()
    return {
        "products" : products
    }

# Mostrar un producto 
@app.get("/api/product/{product_id}/")
async def get_product(product_id: int):
    product = product_controller.getProductById(product_id)
    if product:
        return {
            "ok": True,
        }

# Modificar un producto
@app.put("/api/product/update/{product_id}/")
async def update_product(product_id: int, updated_product_data: dict):

    product_controller.update_product(product_id, updated_product_data)
    return {
        "ok": True
    }

# Borrar un producto
@app.post("/api/product/delete/{product_id}/")
async def delete_product(product_id:int):
    product_controller.Delete_Product(id=product_id)
    print(product_id)
    return{
        "ok" : True
    }
 
# Crear un producto 
@app.post("/api/products/create")
async def create_product(product: Product): # Do not send the id in the request
    product_controller.createProduct(code=product.code, name=product.name, price=product.price)

    return {
        "ok" : True
    }

#################################################

# Crear una venta
@app.post("/api/sale/create")
async def create_sale(machine_id: int, product_id: int): # original
    successfull = sale_controller.create_sale(product_id=product_id, machine_id=machine_id)

    return {
        "success" : successfull 
    }
 
# Modificar una venta

# Borrar una venta

# Leer una venta

# Leer todas las ventas