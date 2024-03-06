from sqlmodel import Field, SQLModel
from typing import Optional

class VendingMachine(SQLModel, table=True):
    __tablename__ = "vendingmachines"
    id: Optional[int] = Field(default=None, primary_key=True)
    