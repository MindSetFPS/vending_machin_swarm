from sqlmodel import Field, SQLModel
from typing import Optional

class VendingMachine(SQLModel, table=True):
    __tablename__ = "vendingmachines"
    id: Optional[int] = Field(default=None, primary_key=True)
    
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

# class VendingMachineMoneyLink(SQLModel, table=True):
#     machine_id: int
#     denomination_id: int
#     stock: int