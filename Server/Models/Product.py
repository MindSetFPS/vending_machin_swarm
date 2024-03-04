from ..Repository.SQLBase import Base

from sqlalchemy import Column, Integer, String, Uuid, Float

class Product(Base):
    def __init__(self, name: str, price: float, code: str, stock: int ):
        self.name = name 
        self.price = price
        self.code = code 
        self.stock = stock

    __tablename__ = "products"
    id = Column(Uuid, primary_key=True)
    name = Column(String)
    price = Column(Float)

    def clone(self):
        return self
