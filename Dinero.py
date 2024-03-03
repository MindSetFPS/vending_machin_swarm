
class Dinero:
    
    def __init__(self, valor: int, cantidad: int ,tipo: str):
        self.valor = valor
        self.cantidad = cantidad
        self.tipo = tipo
    #debe de de regresar un valor dienero    
    def clone (self):
        return (self)
        
dinero = Dinero(valor=10, cantidad=10, tipo="Moneda")

print(type(dinero.clone()))