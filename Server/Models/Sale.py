from sqlalchemy import Column, Integer, String, Uuid, DateTime, ForeignKey
from ..Repository.SQLBase import Base

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Uuid, primary_key=True)
    date = Column(DateTime)
    product = Column(Uuid, ForeignKey("products.id"))