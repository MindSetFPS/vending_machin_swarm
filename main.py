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
@app.get("/api/products")
async def get_all_products():
    products = product_controller.get_all_products()
    return {
        "products" : products
    }
# Mostrar un producto 
@app.get("/api/product/{product_id}/")
async def get_product(product_id: int):
    product = product_controller.get_product_by_id(product_id)
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
