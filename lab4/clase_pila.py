# -*- coding: utf-8 -*-
"""
Clase Pila/Stack

@author: Jesus Albert
@date: 20/03/2022
"""

class Pila:
    """
    Clase pila de elementos.
    Resumen de operaciones públicas:
        def __init__(self): Constructor
        def Apilar(self,x): Añadir x a la pila
        def Desapilar(self): Eliminar último elemento
        def Cima(self)->elemento: Consultar último elemento
        def EsVacia(self)->bool: Determinar si hay elementos
        def __str__ (self)->str: Versión str de la pila
    """

    def __init__(self):
        """
        Constructor

        Returns
        -------
        None.

        """
        self.__elementos = []
    
    def Apilar(self,x):
        """
        Añadir x al final de la pila 

        Parameters
        ----------
        x : Elemento añadido.

        Returns
        -------
        None.

        """
        self.__elementos.append(x)
        
    def Desapilar(self):
        """
        Eliminar el último elemento de la pila

        Raises
        ------
        RuntimeError
            Si la pila está vacía y no se puede eliminar.

        Returns
        -------
        None.

        """
        if self.EsVacia(): # no se puede eliminar
            raise RuntimeError("Desapilar: Intento de eliminar en pila vacía.")
        self.__elementos.pop()
    
    def Cima(self):
        """
        Consultar el valor del último elemento de la pila

        Raises
        ------
        RuntimeError
            Si la pila está vacía y no se puede consultar.

        Returns
        -------
        Último elemento de la pila.

        """
        if self.EsVacia(): # no se puede consultar la cima
            raise RuntimeError("Cima: Intento de consultar en pila vacía.")
        ultimo = len(self.__elementos)-1
        return self.__elementos[ultimo]
    
    def EsVacia(self)->bool:
        """
        Determinar si la pila está vacía

        Returns
        -------
        bool
            True si la pila está vacía.
            False si hay elementos en la pila.

        """
        return len(self.__elementos) == 0
    
    def __str__ (self)->str:
        """
        Generar string con el contenido de la pila

        Returns
        -------
        s : str
            Cadena con la información de los elementos de la pila.
            En primer lugar la cima de la pila, en el último el fondo.

        """
        if self.EsVacia():
            s = "Pila Vacia"
        else:
            i = len(self.__elementos)-1
            s = ""
            while i >= 0:
                s += str(self.__elementos[i]) + "\n"
                i -= 1
        return s
