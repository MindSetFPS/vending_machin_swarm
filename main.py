from Server.Product.application.ProductController import product_controller
from Server.Product.domain.Product import Product
from Server.Incident import incident
from Server.VendingMachine.application import route as VendingMachineRouter
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Server.Sale.application import route as SaleRouter
from Server.Product.application import route as ProductRouter

app = FastAPI()

app.include_router(router=incident.router)
app.include_router(router=VendingMachineRouter.router)
app.include_router(router=SaleRouter.router)
app.include_router(router=ProductRouter.router)

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