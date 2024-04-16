from clase_cuenta_bancaria import CuentaBancaria
from clase_iban import IBAN
from clase_cola import Cola

unpaidRecipts = []
notFoundAccounts = []
paidRecipts = 0

def ReadAccounts(name: str) -> (bool, list):
	opened = False
	accounts = []
	try:
		f = open(name, encoding="utf-8")
	except FileNotFoundError:
		print(f"File not found: {name}")
	else:
		opened = True
		for line in f:
			line = line.rstrip("\n")
			splittedLine = line.split(";")
			accounts.append(CuentaBancaria(IBAN(splittedLine[0]), splittedLine[1], float(splittedLine[2])))
		f.close()
	return opened, accounts

def ReadRecipts(name: str) -> (bool, Cola):
	opened = False
	recipts = Cola()
	try:
		f = open(name, encoding="utf-8")
	except FileNotFoundError:
		print(f"File not found: {name}")
	else:
		opened = True
		for line in f:
			line = line.rstrip("\n")
			splittedLine = line.split(";")
			recipts.Encolar(splittedLine)
		f.close()
	return opened, recipts

def searchIBAN(accounts: list, iban: str) -> int:
	for index, account in enumerate(accounts):
		if account.GetIBAN().__eq__(IBAN(iban)):
			return index
	return -1


def CobrarRecibos(accounts: list, recipts: Cola):
	global paidRecipts
	while not recipts.EsVacia():
		recipt = recipts.Primero()
		result = searchIBAN(accounts, recipt[0])
		if result != -1:
			try:
				accounts[result].Retirar(float(recipt[1]), "Recibo de energía")
				paidRecipts += 1
			except RuntimeError as e:
				if e.args[0] == "Insufficient funds in the account":
					unpaidRecipts.append(recipt)
				else:
					print(e)
		else:
			notFoundAccounts.append(recipt)
		recipts.Desencolar()
		

def main():
	accountsFilename = "cuentas_L1.dat"
	cuentas = ReadAccounts(accountsFilename)
	# print("Accounts: \n")
	# if cuentas[0]:
	# 	for c in cuentas[1]:
	# 		print(c)
 
	reciptsFilename = "recibos_L1.dat"
	recipts = ReadRecipts(reciptsFilename)
	# if recipts[0]:
	# 	print("Recipts: \n")
	# 	count = 0
	# 	reciptsList = copy.deepcopy(recipts[1])
	# 	while not reciptsList.EsVacia() and count < 10:
	# 		print(reciptsList.Primero())
	# 		reciptsList.Desencolar()
	# 		count += 1

	if cuentas[0] and recipts[0]:
		CobrarRecibos(cuentas[1], recipts[1])
		print("Recibos cobrados correctamente: " + str(paidRecipts))
		print("Recibos impagados por falta de saldo: " + str(len(unpaidRecipts)))
		print("Recibos impagados por error en la cuenta: " + str(len(notFoundAccounts)) + "\n")
		for c in cuentas[1]:
			print("Datos de la cuenta: " + c.GetIBAN().__str__())
			print(c.GetTitular())
			print("Saldo: " + str(c.GetSaldo()) +"EUR")
			print("== Operaciones ==")
			c.MostrarOperaciones()


if __name__ == '__main__':
	main()