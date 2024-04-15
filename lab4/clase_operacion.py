# -*- coding: utf-8 -*-
"""
@author: Jesus Albert

Práctica Nº 5 EDA: Clase OperacionBancaria
CLASE PROPORCIONADA A LOS ESTUDIANTES
"""

""" Clase OperacionBancaria que representa una operación sobre la cuenta de 
un cliente de un banco (ingreso o reintegro)"""
class OperacionBancaria:

    def __init__ (self, imp: int, con:str):
        """
        Constructor de la clase
        Se le pasan los datos de la operación

        Parameters
        ----------
        imp : int
            Importe de la operación (>0 = ingreso, <0 = reintegro)
        con : str
            Concepto de la operación (texto)

        Returns
        -------
        None.

        """
        self.__importe = imp
        self.__concepto = con
        
    def GetImporte(self)->int:
        """
        Obtener el importe de la operación

        Parameters
        ----------

        Returns
        -------
        int
            importe

        """
        return self.__importe
        
    def GetConcepto(self)->str:
        """
        Obtener el concepto de la operación

        Parameters
        ----------

        Returns
        -------
        str
            concepto

        """
        return self.__concepto
        
    def __str__(self)->str:
        """
        Convertir la operación en cadena de caracteres

        Returns
        -------
        str
            Cadena con los datos de la operación

        """
        s = str()
        if self.__importe > 0:
            s += "Ingreso: "
        elif self.__importe < 0:
            s += "Reintegro: "
        s += str(self.__importe) + " EUR"
        s += " (" + self.__concepto + ")"
        return s