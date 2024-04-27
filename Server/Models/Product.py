from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from Server.VendingMachine.domain.VendingMachine import VendingMachineProductsLink

class Product(SQLModel, table=True):

    __tablename__ = "products"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    code: str
    vending_machines: List["VendingMachine"] = Relationship(back_populates="products", link_model=VendingMachineProductsLink)

    def clone(self):
        return self