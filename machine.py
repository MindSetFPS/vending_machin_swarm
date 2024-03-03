from Dinero import Dinero 
from Producto import Producto
from Monedero import Monedero



class Maquina:

    def __init__(self, SelectedProductCode: str, balance: int ):
        self.SelectedProductCode = SelectedProductCode
        self.balance = balance

    def __init__(self):
        self.selected_product_code = None
        self.balance = 0
        self.monedero = Monedero([
            Dinero(valor=1, cantidad=50, tipo="Moneda"),
            Dinero(valor=2, cantidad=50, tipo="Moneda"),
            Dinero(valor=5, cantidad=50, tipo="Moneda"),
            Dinero(valor=10, cantidad=0, tipo="Moneda"),
            Dinero(valor=20, cantidad=0, tipo="Billete"),
            Dinero(valor=50, cantidad=0, tipo="Billete"),
        ])
        self.products = [
            Producto(code="A1", name="Papitas", price=15, stock=10),
            Producto(code="A2", name="Jugo de Naranja", price=20, stock=10),
            Producto(code="A3", name="Café con leche", price=35, stock=10),
            Producto(code="A4", name="Mantecadas", price=28, stock=10),
            Producto(code="B1", name="Bizcochitos", price=12, stock=1),
            Producto(code="B2", name="Gansito", price=21, stock=10)
        ]

    def machine_loop(self):
        while True:
            self.show_products()
            self.verify_selected_product_code()
            time.sleep(6)
            self.clear_console()

    def show_products(self):
        accepts = "Acepta denominacion de "
        for dinero in self.monedero.available_denominations:
            accepts += f"${dinero.valor} "
        print(accepts)
        for product in self.products:
            print(f"Codigo: {product.code} - {product.name} - ${product.price} - Stock:{product.stock}")

    def verify_selected_product_code(self):
        self.selected_product_code = input()
        selected_product = next((product for product in self.products if product.code == self.selected_product_code), None)

        if selected_product is None or selected_product.stock == 0:
            print("Intenta de nuevo")
            self.verify_selected_product_code()
        else:
            drop_product = self.receive_balance(selected_product.price)
            if drop_product:
                self.update_stock(selected_product)

    def receive_balance(self, product_price):
        print("Por favor inserta tu saldo")
        inserted_balance = 0
        while product_price > inserted_balance:
            self.balance = int(input())
            balance_is_in_denominations = "si" if self.monedero.received_balance_is_in_denominations(inserted_balance=self.balance) else "no"
            if self.monedero.received_balance_is_in_denominations(inserted_balance=self.balance):
                inserted_balance += self.balance
                print(f"Has insertado ${inserted_balance}")
            else:
                print("No aceptamos esa denominacion. Prueba con otra.")

        drop_product = False
        if inserted_balance == product_price:
            print("Entregar producto")
            drop_product = True

        if inserted_balance > product_price:
            if self.monedero.total_money == 0:
                print("Lo siento, en este momento no tenemos las monedas para darte cambio, intenta ingresando el saldo exacto.")
            else:
                drop_product = self.monedero.can_give_change(price=product_price, balance=inserted_balance)

        return drop_product

    def update_stock(self, product):
        product.stock -= 1

    @staticmethod
    def clear_console():
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    maquina = Maquina()
    maquina.machine_loop()