from fastapi import APIRouter
from .SaleController import sale_controller

router = APIRouter(
    prefix="/api/sale",
    tags=["sales"]
)

# Crear una venta
@router.post("/api/sale/create")
async def create_sale(machine_id: int, product_id: int): # original
    successfull = sale_controller.create_sale(product_id=product_id, machine_id=machine_id)
    return {
        "success" : successfull 
    }
 
# Modificar una venta

# Borrar una venta

# Obtener una venta
@router.get("/api/sale/{sale_id}")
async def get_sale(sale_id: int):
    sale = sale_controller.get_sale_by_id(sale_id=sale_id)
    return sale

# Leer todas las ventas
@router.get("/api/sales")
async def get_sales():
    sales = sale_controller.get_sales()
    return sales

# Obtener ventas por maquina
@router.get("/api/sales/machine/{machine_id}")
async def get_sales_by_machine_id(machine_id: int):
    sales = sale_controller.get_sales_by_machine_id(machine_id=machine_id)
    sales_json = [] 
    for sale, product in sales:

        sales_json.routerend({
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