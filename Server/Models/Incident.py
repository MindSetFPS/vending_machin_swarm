from sqlmodel import Field, SQLModel, Enum
from typing import Optional

class Status(str, Enum):
    refill_requested = 'A refill has been requested.'
    refill_required = 'A product in the machine needs a refill.'

class Incident (SQLModel, table=True):
    __tablename__ = "incidents"
    id: Optional[int] = Field(default=None, primary_key=True) 
    description: str
    fix_at_url: Optional[str] = Field(default=None, primary_key=False)
    active: bool
    machine_id: Optional[int] = Field(default=None, primary_key=False)
    product_id: Optional[int] = Field(default=None, primary_key=False)