from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
    
class VendingMachineProductsLink(SQLModel, table=True):
    machine_id: Optional[int] = Field(
        default=None,
        foreign_key="vendingmachines.id",
        primary_key=True
    )
    product_id: Optional[int] = Field(
        default=None,
        foreign_key="products.id",
        primary_key=True
    )
    stock: int

class VendingMachine(SQLModel, table=True):
    __tablename__ = "vendingmachines"
    id: Optional[int] = Field(default=None, primary_key=True)
    is_on: bool
    products: List['Product'] = Relationship(back_populates="vending_machines", link_model=VendingMachineProductsLink)

# class VendingMachineMoneyLink(SQLModel, table=True):
#     machine_id: int
#     denomination_id: int
#     stock: int