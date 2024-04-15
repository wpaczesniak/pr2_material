# -*- coding: utf-8 -*-
"""
@author: Jesus Albert

Práctica Nº 5 EDA: Clase IBAN
CLASE PROPORCIONADA A LOS ESTUDIANTES
"""

""" Clase IBAN que representa el International Bank Account Number,
formato internacional para identificar cuentas bancarias """
class IBAN:

    def __init__ (self, iban:str):
        """
        Constructor
        Se le pasa la cadena con el códigon y se realizan validaciones
        antes de registrarlo

        Parameters
        ----------
        iban : str
            Cadena de texto con el código

        Raises
        ------
        RuntimeError
            En caso de que la cadena pasada no cumpla alguno de los criterios
            de validación

        Returns
        -------
        None.

        """
        if IBAN.__Validar(iban):
            self.__iban = iban
        else: 
            """Excepción si el formato es incorrecto """
            raise RuntimeError ("IBAN: Error de codificación.")
    
    def GetPais (self)->str:
        """
         Obtener código de pais de la cuenta

        Returns
        -------
        str
            código del país

        """
        return self.__iban[:2]
    
    def GetControlIBAN (self)->str:
        """
        Obtener código de control IBAN de la cuenta

        Returns
        -------
        str
            código de control

        """
        return self.__iban[2:4]
    
    def GetEntidad (self)->str:
        """
        Obtener código de entidad financiera de la cuenta

        Returns
        -------
        str
            código de entidad financiera

        """
        return self.__iban[4:8]
    
    def GetOficina (self)->str:
        """
        Obtener código de oficina (de la entidad) de la cuenta 

        Returns
        -------
        str
            código de oficina (de la entidad)

        """
        return self.__iban[8:12]
    
    def GetControlEntidad (self)->str:
        """
        Obtener código de control de la entidad de la cuenta

        Returns
        -------
        str
            código de control de la entidad

        """
        
        return self.__iban[12:14]
    
    def GetNumCuenta (self)->str:
        """
        Obtener número de la cuenta

        Returns
        -------
        str
            número de la cuenta


        """
        return self.__iban[14:]
    
    def __str__ (self)->str:
        """
        Versión str del código de cuenta.
        Formato imprimible en grupos de 4 caracteres.

        Returns
        -------
        str
            Texto con el código IBAN formateado

        """
        sep = " "     
        s = ""
        ini = 0
        while ini < len(self.__iban) - 4:
            s += self.__iban[ini:ini+4] + sep
            ini = ini + 4
        return s
    
    def __eq__ (self, otro)->bool:
        """
        Sobrecarga del operador == para comparar dos objetos IBAN

        Parameters
        ----------
        otro : IBAN
            segundo objeto de la comparación

        Returns
        -------
        bool
            True = iguales, False = distintos

        """
        return self.__iban == otro.__iban

    def __Validar(codigo:str)->bool:
        """
        Validación simple del formato IBAN.
        Solo valida que:
            El código tenga 24 caracteres
            El país sea España
            Los caracteres de 2:24 son digitos.
        No comprueba la corrección de los códigos de control.

        Parameters
        ----------
        codigo : str
            código a validar

        Returns
        -------
        bool
            True = Correcto, False = Incorrecto

        """
        correcto = False
        if len(codigo) == 24:
            if codigo[:2] == "ES":
                i = 2
                correcto = True
                while i < len(codigo) and correcto:
                    if codigo[i] in "0123456789":
                        i += 1
                    else:
                        correcto = False
        return correcto

def main():
    try:
        a = IBAN("ES9820385778983000760236") # Correcta
    except RuntimeError as e:
        print(e)
        print("Test 1: Error. Detectada excepción.")
    else:
        print("Test 1: OK")
        print(a)
    print()
    try:
        b = IBAN("ES1033878296295191603012") # Correcta
    except RuntimeError as e:
        print(e)
        print("Test 2: Error. Detectada excepción.")
    else:
        print("Test 2: OK")
        print(b)
    print()
    try:
        c = IBAN("E1100492352082414205416") # Incorrecta
    except RuntimeError as e:
        print(e)
        print("Test 3: OK. Detectada excepción.")
    else:
        print("Test 3: Error. Excepción no detectada.")
        print(c)
    return

if __name__ == "__main__":
    main()
