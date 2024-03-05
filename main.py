from fastapi import FastAPI
from Server.Repository.ProductRepository import product_repository

app = FastAPI()

@app.get("/")
async def root():
    product_repository.get_all_items()
    return {
        "message" : "Hello World"
    }

@app.get("/api/machines")
async def vending_machines():
    return {
        "machines" : "true"
    }

# 1. Register machines

# 2. Register products 

# 3. Reister sales

# 4. List Machines ( Sort by cash sales )