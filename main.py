from fastapi import FastAPI, Request
from Server.Repository.ProductRepository import product_repository
from Server.Controllers.ProductController import product_controller
from Server.Controllers.SaleController import sale_controller 
from Server.Controllers.VendingMachineController import vending_machine_controller
from Server.Models.Product import Product
from Server.Models.VendingMachine import VendingMachine
from typing import Optional
import json

app = FastAPI()

@app.get("/")
async def root():
    product_repository.get_all_items()
    return {
        "message" : "Hello World"
    }

# Listar todas maquinas
@app.get("/api/machines")
async def vending_machines():
    return {
        "machines" : "true"
    }

# Listar una maquina

# Modificar una maquina

# Borrar una maquina

# Crear una maquina (en el servidor)
@app.post("/api/vendingmachine/create")
async def create_vending_machine(vendingMachine: VendingMachine):
    vending_machine_controller.create_vendingmachine()
    print(vendingMachine.id)
    return {
        "ok": "True"
    }

#################################################

# Listar todos los productos

@app.get("/api/products")
async def get_all_products():
    products = product_controller.get_all_products()
    return {
        "products" : products
    }

# Mostrar un producto 

# Modificar un producto

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
async def create_product(product: Product):
    product_controller.createProduct(code=product.code, name=product.name, price=product.price)

    return {
        "ok" : True
    }

#################################################

# Crear una venta

@app.post("/api/sale/create")
# The AI helped me solve this lol
async def create_sale(product_id: Request): # original
# async def create_sale(product_id: Optional[int] = None):
    r = await product_id.json()
    print(r['product_id'])
    sale_controller.create_sale(product_id=r['product_id'])
    return {
        "ok": True
    }
 
# Modificar una venta

# Borrar una venta

# Leer una venta

# Leer todas las ventas