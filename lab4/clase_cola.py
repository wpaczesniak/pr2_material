# -*- coding: utf-8 -*-
"""
Clase Cola/Queue
Implementada con deque

@author: Jesus Albert
@date: 20/03/2022
"""

from collections import deque

class Cola:
    """
    Clase cola de elementos.
    Resumen de operaciones públicas:
        def __init__(self): Constructor
        def Encolar(self,x): Añadir x a la cola
        def Desencolar(self): Eliminar primer elemento
        def Primero(self)->elemento: Consultar primer elemento
        def EsVacia(self)->bool: Determinar si hay elementos
        def __str__ (self)->str: Versión str de la cola
    """
    
    def __init__(self):
        """
        Constructor

        Returns
        -------
        None.

        """
        self.__elementos = deque()
       
    def Encolar(self,x): 
        """
        Añadir x al final de la cola 

        Parameters
        ----------
        x : Elemento añadido.

        Returns
        -------
        None.

        """
        self.__elementos.append(x)
        
    def Desencolar(self): 
        """
        Eliminar el primer elemento de la cola

        Raises
        ------
        RuntimeError
            Si la cola está vacía y no se puede eliminar.

        Returns
        -------
        None.

        """
        if self.EsVacia():
            raise RuntimeError("Desencolar: Intenta eliminar en cola vacía")
        self.__elementos.popleft()
    
    def Primero(self):
        """
        Consultar el valor del primer elemento de la cola

        Raises
        ------
        RuntimeError
            Si la cola está vacía y no se puede consultar.

        Returns
        -------
        Primer elemento de la cola.

        """
        if self.EsVacia():
            raise RuntimeError("Primero: Intenta consultar en cola vacía")
        return self.__elementos[0]

    def EsVacia(self)->bool:
        """
        Determinar si la cola está vacía

        Returns
        -------
        bool
            True si la cola está vacía.
            False si hay elementos en la cola.

        """
        return len(self.__elementos) == 0

    def __str__ (self)->str:
        """
        Generar string con el contenido de la cola

        Returns
        -------
        s : str
            Cadena con la información de los elementos de la cola.

        """
        if self.EsVacia():
            s = "Cola Vacia"
        else:
            i = 0
            ultimo = len(self.__elementos)
            s = ""
            while i < ultimo:
                s += str(self.__elementos[i]) + "\n"
                i += 1
        return s
