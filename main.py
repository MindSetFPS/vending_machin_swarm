from Server.Controllers.ProductController import product_controller
from Server.Controllers.SaleController import sale_controller 
from Server.Models.Product import Product
from Server.Incident import incident
from Server.VendingMachine.application import route as VendingMachineRouter
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(router=incident.router)
app.include_router(router=VendingMachineRouter.router)


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