# -*- coding: utf-8 -*-
"""
@author: Jesus Albert

Práctica Nº 5 EDA: Test de la clase CuentaBancaria
CLASE PROPORCIONADA A LOS ESTUDIANTES
"""

""" IMPORTANTE: Indicar el nombre correcto del archivo donde está tu clase """
from clase_cuenta_bancaria import CuentaBancaria

from clase_iban import IBAN

def Test_0(cuentas:list):
    print("Test 0: Crear 3 cuentas iniciales")
    print("Las 2 primeras son correctas y la última incorrecta")
    print()
    ok = True
    #1
    try:
        s = "ES9820385778983000760236"
        print("Crear cuenta correcta:",s)
        iban1 = IBAN(s) # Correcto
        c1 = CuentaBancaria(iban1,"Jesús Albert",100.5)
        cuentas.append(c1)
    except:
        print("Error en IBAN:",s,"(no debería salir)")
        ok = False
    else:
        print("Ok")
    #2    
    try:
        s = "ES1033878296295191603012"
        print("Crear cuenta correcta:",s)       
        iban2 = IBAN(s) # Correcto
        c2 = CuentaBancaria(iban2,"Elena García",2000)
        cuentas.append(c2)
    except:
        print("Error en IBAN:",s,"(no debería salir)")
        ok = False
    else:
        print("Ok")
    #3
    try:
        s = "E1100492352082414205416"
        print("Intentar crear cuenta incorrecta:",s)        
        iban3 = IBAN(s) # Incorrecto
        c3 = CuentaBancaria(iban3,"Paco Castro",500)    
        cuentas.append(c3)
    except:
        print("Error en IBAN:",s,"(Ok)")
    else:
        print("Incorrectamente creada. CORREGIR ERROR")
        ok = False
    print()
    print("Resultado del Test 0: ",end="")
    if ok:
        print("Finalizado CORRECTAMENTE.")
    else:
        print("Algo ha fallado.")

def Test_1(cuentas:list):
    print("Test 1: Mostrar cuentas iniciales usando __str__ ")
    print("="*30)
    for c in cuentas:
        print(c)
        print()

def Test_2(cuentas:list):
    print("Test 2: Mostrar cuentas iniciales usando GET")
    print("="*30)
    for c in cuentas:
        print("IBAN:", c.GetIBAN())
        print("Titular:", c.GetTitular())
        print("Saldo:", c.GetSaldo())
        print()

def Test_3(cuentas:list):
    print("Test 3: Ingresos y Reintegros")
    print("="*30)
    print("Realizar ingresos de 1000 euros y mostrar cuentas")
    ok = True
    for c in cuentas:
        try:
            c.Ingresar(1000,"Nómina")
        except RuntimeError as e:
            print(e)
            ok = False
        else:
            print("Ok")
            print(c)
            print()

    print("Realizar reintegro de 500 euros y mostrar cuentas")
    for c in cuentas:
        try:
            c.Retirar(500,"Pago")
        except RuntimeError as e:
            print(e)
            ok = False
        else:
            print("Ok")
            print(c)
            print()

    print("Realizar ingreso y reintegro con valores negativos")
    print("Se deben lanzar excepciones")
    """ Ingreso incorrecto en cuentas[0] """
    try:
        cuentas[0].Ingresar(-10,"Pago")
    except RuntimeError as e:
        print(e)
        print("Ok")
    else:
        ok = False
        print("Ingresar incorrecto. CORREGIR ERROR")
        print(cuentas[0])
        print()
    """ Retirada incorrecta en cuentas[1] """
    try:
        cuentas[1].Retirar(-10,"Ingreso")
    except RuntimeError as e:
        print(e)
        print("Ok")
    else:
        ok = False
        print("Retirar incorrecto. CORREGIR ERROR")
        print(cuentas[1])
        print()
        
    print()
    print("Resultado del Test 3: ",end="")
    if ok:
        print("Finalizado CORRECTAMENTE.")
    else:
        print("Algo ha fallado.")

            
def Test_4(cuentas:list):
    print("Test 4: Historial de operaciones")
    print("="*30)
    print("Mostrar el histórico de operaciones de cada cuenta")
    print()
    for c in cuentas:
        print("Operaciones en cuenta de",c.GetTitular())
        c.MostrarOperaciones()
        
def Pausa():
    print()
    input("Pulsar <Enter> ...")
    print()

def main():
    cuentas = []
    print()
    Test_0(cuentas)
    Pausa()
    Test_1(cuentas)
    Pausa()
    Test_2(cuentas)
    Pausa()
    Test_3(cuentas)
    Pausa()
    Test_4(cuentas)
    print()
    print(" *** Fin ***")

if __name__ == "__main__":
    main()
