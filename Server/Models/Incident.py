from sqlmodel import Field, SQLModel, Enum
from typing import Optional
from sqlalchemy import Column

class Warnings(str, Enum):
    Product_Empty = 'Product is Empty'
    Machine_Empty = 'Machine is Empty'

class Incident (SQLModel, table=True):
    __tablename__ = "incidents"
    id: Optional[int] = Field(default=None, primary_key=True) 
    description: str
    fix_at_url: str
    active: bool