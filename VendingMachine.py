from Server.Models.Dinero import Dinero
from Server.Product.domain.Product import Product
from Server.Sale.domain.Sale import Sale
from Server.VendingMachine.domain.VendingMachine import VendingMachine
import time, os, random
import requests
from sqlmodel import Field, SQLModel, create_engine
from Server.Models.Dinero import Dinero
from Server.Product.domain.Product import Product
from Server.Sale.domain.Sale import Sale
from Server.VendingMachine.domain.VendingMachine import VendingMachine
import time, os, random
import requests
from sqlmodel import Field, SQLModel, create_engine
import tkinter as tk
from tkinter import messagebox
import requests

class Product:
    def __init__(self, code, name, price, stock):
        self.code = code
        self.name = name
        self.price = price
        self.stock = stock

class Monedero:
    def __init__(self, machine_id, base_url):
        self.machine_id = machine_id
        self.api = VendingMachineAPI(base_url)
        self.available_denominations = []

    def get_all_products(self):
        products = self.api.get_products_by_id(self.machine_id)
        if products:
            product_objects = [Product(**product) for product in products]
            return product_objects
        else:
            print('Error: La lista de productos está vacía')
            return []

class Maquina:
    def __init__(self, root, id, base_url):
        self.id = id 
        self.root = root
        self.root.title("Máquina Expendedora")
        
        self.selected_product = None
        self.balance = ""  # Inicializar como una cadena vacía
        
        self.monedero = Monedero(id, base_url)
        
        self.create_widgets()

    def create_widgets(self):
        self.display_var = tk.StringVar()
        display = tk.Entry(self.root, textvariable=self.display_var, font=('Helvetica', 20), justify='right')
        display.grid(row=0, column=0, columnspan=4, sticky='ew')
        
        for i in range(10):
            tk.Button(self.root, text=i, font=('Helvetica', 20), command=lambda num=i: self.process_money(num)).grid(row=1, column=i, sticky='nsew')
        
        self.balance_label = tk.Label(self.root, text="Balance: $0", font=('Helvetica', 20))
        self.balance_label.grid(row=2, column=0, columnspan=4, sticky='ew')
        
        products = self.monedero.get_all_products()
        if products:
            print("Productos obtenidos correctamente:", products)  
            for product in products:
                print("Agregando botón para:", product.name)  
                tk.Button(self.root, text=product.name, font=('Helvetica', 20), command=lambda prod=product: self.process_product(prod)).grid(row=3, column=products.index(product), sticky='nsew')
        else:
            messagebox.showerror("Error", "No se pudieron obtener los productos de la máquina.")
            print('Error: No se pudieron obtener los productos de la máquina')

        tk.Button(self.root, text="Proceder con la Compra", font=('Helvetica', 20), command=self.proceed_with_purchase).grid(row=4, column=0, columnspan=4, sticky='ew')

    def process_product(self, product):
        self.selected_product = product
        messagebox.showinfo("Producto Seleccionado", f"Has seleccionado {self.selected_product.name}. Por favor, ingresa el dinero.")

    def update_balance_label(self):
        self.balance_label.config(text=f"Balance: ${self.balance}")

    def proceed_with_purchase(self):
        if self.selected_product:
            if self.selected_product.stock > 0:
                if self.balance >= self.selected_product.price:
                    self.balance -= self.selected_product.price
                    self.selected_product.stock -= 1
                    self.monedero.can_give_change(self.selected_product.price, self.balance) 
                    messagebox.showinfo("Compra Exitosa", f"¡Compra exitosa! Has comprado {self.selected_product.name}. Tu cambio es {self.balance}.")
                    self.selected_product = None
                    self.balance = 0
                    self.update_balance_label()
                else:
                    messagebox.showerror("Error", "Saldo insuficiente. Introduce más dinero.")
            else:
                messagebox.showerror("Error", "Producto agotado.")
        else:
            messagebox.showerror("Error", "Por favor, selecciona un producto primero.")

    def process_money(self, amount):
        self.balance += str(amount)
        self.update_balance_label()

    def update_balance_label(self):
        try:
            balance_value = int(self.balance)
        except ValueError:
            balance_value = 0  
        self.balance_label.config(text=f"Balance: ${balance_value}")
class VendingMachineAPI:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")

    def get_products_by_id(self, machine_id):
        url = f"{self.base_url}/api/vendingmachine/{machine_id}/products"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error al obtener los productos de la máquina {machine_id}: {response.text}")
                return []
        except requests.RequestException as e:
            print(f"Error de conexión: {e}")
            return []

if __name__ == "__main__":
    root = tk.Tk()
    base_url = "http://127.0.0.1:7777"  
    app = Maquina(root, id=123, base_url=base_url) 
    root.mainloop() 
