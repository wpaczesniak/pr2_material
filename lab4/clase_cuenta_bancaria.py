from clase_iban import IBAN
from clase_operacion import OperacionBancaria
from clase_pila import Pila


class CuentaBancaria:
    def __init__(self, iban, titular, saldo):
        self.iban = iban
        self.titular = titular
        if saldo < 0:
            raise RuntimeError("Initial saldo cannot be negative")
        self.saldo = saldo
        self.operaciones = Pila()

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
        self.operaciones.Apilar(OperacionBancaria(amount, concepto))

    def Retirar(self, amount, concepto):
        if amount <= 0:
            raise RuntimeError("Withdrawal amount must be positive")
        if self.saldo < amount:
            raise RuntimeError("Insufficient funds in the account")
        self.saldo -= amount
        self.operaciones.Apilar(OperacionBancaria(-amount, concepto))

    def MostrarOperaciones(self):
        if self.operaciones.EsVacia():
            print("No hay operaciones registradas.")
        else:
            print(self.operaciones)
            





    def __str__(self):
        formatted_iban = str(self.iban)
        return f"IBAN: {formatted_iban}, Account Holder: {self.titular}, saldo: {self.saldo} EUR"