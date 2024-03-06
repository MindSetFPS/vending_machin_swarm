from typing import Optional
from sqlmodel import Field, SQLModel

class Product(SQLModel, table=True):
    def __init__(self, name: str, price: float, code: str ):
        self.name = name 
        self.price = price
        self.code = code 

    __tablename__ = "products"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    code: str

    def clone(self):
        return self