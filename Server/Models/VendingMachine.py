from Server.Repository.SQLBase import Base

from sqlalchemy import Column, Uuid

class VendingMachine(Base):
    __tablename__ = "vendingmachines"
    id = Column(Uuid, primary_key=True)