from fastapi import APIRouter

from .ProductController import product_controller
from Server.Product.domain.Product import Product

router = APIRouter(
    prefix="/api/product",
    tags=["products"]
)

# Listar todos los productos
@router.get("/api/products")
async def get_all_products():
    products = product_controller.get_all_products()
    return {
        "products" : products
    }

# Mostrar un producto 
@router.get("/api/product/{product_id}/")
async def get_product(product_id: int):
    product = product_controller.getProductById(product_id)
    if product:
        return product

# Modificar un producto
@router.put("/api/product/update/{product_id}/")
async def update_product(product_id: int, updated_product_data: dict):

    product_controller.update_product(product_id, updated_product_data)
    return {
        "ok": True
    }

# Borrar un producto
@router.post("/api/product/delete/{product_id}/")
async def delete_product(product_id:int):
    product_controller.Delete_Product(id=product_id)
    print(product_id)
    return{
        "ok" : True
    }
 
# Crear un producto 
@router.post("/api/products/create")
async def create_product(product: Product): # Do not send the id in the request
    product_controller.createProduct(code=product.code, name=product.name, price=product.price)

    return {
        "ok" : True
    }

