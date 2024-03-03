class Monedero:
    
    def __init__(self, dinero_list):
        self.available_denominations = dinero_list

    def received_balance_is_in_denominations(self, inserted_balance):
        denominations = [dinero.valor for dinero in self.available_denominations]
        return inserted_balance in denominations
    def total_money(self):
        return sum(d.valor * d.cantidad for d in self.available_denominations)

    def can_give_change(self, price, balance):
        # Lógica para dar cambio
        return True 