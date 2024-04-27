from Server.Controllers.ProductController import product_controller
from Server.Models.Product import Product
from Server.Incident import incident
from Server.VendingMachine.application import route as VendingMachineRouter
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Server.Sale.application import route as SaleRouter

app = FastAPI()

app.include_router(router=incident.router)
app.include_router(router=VendingMachineRouter.router)
app.include_router(router=SaleRouter.router)

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