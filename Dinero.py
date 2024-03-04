from sqlalchemy import Column, Integer, String
from SQLBase import Base

# Inheriting Base so that this class is considered a Table in our database
class Dinero (Base):
    def __init__(self, valor: int, cantidad: int ,tipo: str):
        self.valor = valor
        self.cantidad = cantidad
        self.tipo = tipo
    
    #Declaring database table properties
    __tablename__ = "denominations"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def clone (self):
        return (self)
        