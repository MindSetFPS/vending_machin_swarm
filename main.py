from Server.Repository.ProductRepository import product_repository

from Server.Controllers.ProductController import product_controller
from Server.Controllers.SaleController import sale_controller 
from Server.VendingMachine.application.VendingMachineController import vending_machine_controller
from Server.Controllers.VendingMachineProductStockController import vending_machine_product_stock_controller
from Server.Incident.application.IncidentController import incident_controller 
from Server.Incident.domain.Incident import Incident, Status
from Server.Models.Product import Product
from Server.VendingMachine.domain.VendingMachine import VendingMachine, VendingMachineProductsLink
from Server.Models.Sale import Sale
from Server.Incident import incident

from fastapi import FastAPI, Request, Body
from typing import List, Annotated
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(router=incident.router)

origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

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

# Listar una maquina
@app.get("/api/vendingmachine/{id}")
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
@app.get("/api/vendingmachine/{machine_id}/products")
async def get_products_by_vending_machine(machine_id: int):
    vending_machine = vending_machine_controller.get_vending_machine_by_id(id=machine_id)

    if not vending_machine:
        return {
            "error" : "No such vending machine"
        }
    
    vending_machine_products_list = vending_machine_product_stock_controller.get_products_by_machine_id(machine_id=machine_id)
    return vending_machine_products_list

# Modificar una maquina
@app.post("/api/vendingmachine/update")
async def update_vending_machine(id: int, is_on: bool):
    vending_machine_controller.update_vending_machine(id=id, is_on=is_on)
    return {
        'machine' : 'true'
    }

# Rellenar una maquina
@app.post("/api/vendingmachine/refill")
async def refill_vending_machine(vending_machine_stock: VendingMachineProductsLink):
        print(type(vending_machine_stock.stock))
        vending_machine_product_stock_controller.refill_vending_machine(machine_id=vending_machine_stock.machine_id, product_id=vending_machine_stock.product_id, stock=int(vending_machine_stock.stock))

# Asignar productos a una maquina
@app.post("/api/vendingmachine/assign/{machine_id}")
async def assign_products_to_vending_machine(products: List[int], machine_id: int):
    for product_id in products:
        vending_machine_product_stock_controller.refill_vending_machine(machine_id=machine_id, product_id=product_id, stock=0)
        incident_controller.create_incident(incident=Incident(description=Status.refill_required, active=True, product_id=product_id, machine_id=machine_id))
    
    return {
        "ok": True
    }

# Crear una maquina (en el servidor)
@app.post("/api/vendingmachine/create")
async def create_vending_machine(vendingMachine: VendingMachine):
    vending_machine_controller.create_vendingmachine(vendingMachine)
    return {
        "ok": "True"
    }

# Borrar una maquina
@app.delete("/api/vendingmachine/delete/{id}")
async def delete_vending_machine(id: int):
    vending_machine_controller.delete_vending_machine(id=id)
    return {
        "we": "did_something"
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
        return product

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

# Obtener una venta
@app.get("/api/sale/{sale_id}")
async def get_sale(sale_id: int):
    sale = sale_controller.get_sale_by_id(sale_id=sale_id)
    return sale

# Leer todas las ventas
@app.get("/api/sales")
async def get_sales():
    sales = sale_controller.get_sales()
    return sales

# Obtener ventas por maquina
@app.get("/api/sales/machine/{machine_id}")
async def get_sales_by_machine_id(machine_id: int):
    sales = sale_controller.get_sales_by_machine_id(machine_id=machine_id)
    sales_json = [] 
    for sale, product in sales:

        sales_json.append({
            "sale": {
                "id": sale.id,
                "machine_id": sale.machine_id,
                "date": sale.date,
                "product": {
                    "id": product.id,
                    "name": product.name,
                    "price": product.price #Note: make price in a per machine basis
                }
            }
        })
    return sales_json