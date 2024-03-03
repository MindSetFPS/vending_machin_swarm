class Producto:
    
    def __init__(self, name: str, price: float, code: str, stock: int ):
        self.name = name 
        self.price = price
        self.code = code 
        self.stock = stock

    def clone(self):
        return self
