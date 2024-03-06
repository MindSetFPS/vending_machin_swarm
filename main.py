from fastapi import FastAPI
from Server.Repository.ProductRepository import product_repository
from Server.Controllers.ProductController import product_controller
from Server.Models.Product import Product

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

#################################################

# Listar todos los productos

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
    print(product)

    return {
        "ok" : True
    }

#################################################

# Crear una venta

# Modificar una venta

# Borrar una venta

# Leer una venta

# Leer todas las ventas
