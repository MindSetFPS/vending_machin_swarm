from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from datetime import datetime
from Server.Models.Product import Product

class Sale(SQLModel, table=True):
    __tablename__ = "sales"
    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    product_id: int = Field(default=None, foreign_key="products.id")
    product: Optional[Product] = Relationship()
 
    machine_id: int = Field(default=None, foreign_key="vendingmachines.id")