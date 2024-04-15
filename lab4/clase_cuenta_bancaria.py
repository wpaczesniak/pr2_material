from clase_iban import IBAN
from clase_operacion import OperacionBancaria
from clase_pila import Pila


class CuentaBancaria:
    def __init__(self, iban, titular, saldo):
        self.iban = iban  # Użycie klasy IBAN
        self.titular = titular
        if saldo < 0:
            raise RuntimeError("Initial saldo cannot be negative")
        self.saldo = saldo
        self.operaciones = Pila()  # Pila do przechowywania operacji

    def GetIBAN(self):
        return self.iban

    def GetTitular(self):
        return self.titular

    def GetSaldo(self):
        return self.saldo

    def Ingresar(self, amount, concepto):
        if amount <= 0:
            raise RuntimeError("Deposit amount must be positive")
        self.saldo += amount
        self.operaciones.Apilar(OperacionBancaria(amount, concepto))  # Zapis operacji

    def Retirar(self, amount, concepto):
        if amount <= 0:
            raise RuntimeError("Withdrawal amount must be positive")
        if self.saldo < amount:
            raise RuntimeError("Insufficient funds in the account")
        self.saldo -= amount
        self.operaciones.Apilar(OperacionBancaria(-amount, concepto))  # Zapis operacji jako kwota negatywna

    def MostrarOperaciones(self):
        if self.operaciones.EsVacia():
            print("No hay operaciones registradas.")
        else:
            print(self.operaciones)  # Wypisanie historii operacji od najnowszej do najstarszej
            





    def __str__(self):
        formatted_iban = str(self.iban)  # Wywołanie __str__ klasy IBAN
        return f"IBAN: {formatted_iban}, Account Holder: {self.titular}, saldo: {self.saldo} EUR"

# exercise 1

# class CuentaBancaria:
#     def __init__(self, iban, titular, saldo):
#         self.iban = IBAN(iban)  # Using the IBAN class
#         self.titular = titular
#         if saldo < 0:
#             raise ValueError("Initial saldo cannot be negative")
#         self.saldo = saldo

#     def GetIBAN(self):
#         return self.iban

#     def GetTitular(self):
#         return self.titular

#     def Getsaldo(self):
#         return self.saldo

#     def Deposit(self, amount):
#         if amount <= 0:
#             raise ValueError("Deposit amount must be positive")
#         self.saldo += amount

#     def Withdraw(self, amount):
#         if amount <= 0:
#             raise ValueError("Withdrawal amount must be positive")
#         if self.saldo < amount:
#             raise ValueError("Insufficient funds in the account")
#         self.saldo -= amount

#     def __str__(self):
#         formatted_iban = str(self.iban)  # Calling __str__ of the IBAN class
#         return f"IBAN: {formatted_iban}, Account Holder: {self.titular}, saldo: {self.saldo} EUR"

# # Example of use:
# c = CuentaBancaria("ES9820385778983000760236", "P. Perez", 1000)
# print(c)  # Displays initial account information

# c.Deposit(500)
# print(c.Getsaldo())  # Should display 1500

# c.Withdraw(300)
# print(c.Getsaldo())  # Should display 1200


#  test - exercise 1

# Example of use:
# s = "ES9820385778983000760236"
# ibannn = IBAN(s)
# c = CuentaBancaria(ibannn,"Jesús Albert",100.5)
# print(c)  # Displays initial account information

# c.Ingresar(500, "add")
# print(c.GetSaldo())  # Should display 1500

# c.Retirar(300, "sub")
# print(c.GetSaldo())  # Should display 1200

# c.MostrarOperaciones()  # Should display the history of operations