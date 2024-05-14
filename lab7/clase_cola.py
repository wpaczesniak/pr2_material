# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:06:25 2019

Clase Cola/Queue

@author: Jesus Albert
"""

from collections import deque

class Cola:
    def __init__(self):
        self.__elementos = deque()
       
    def Encolar(self,x): 
        """ Añadir x al final de la cola """
        self.__elementos.append(x)
        
    def Desencolar(self): 
        """ Eliminar el primer elemento de la cola """
        if self.EsVacia():
            raise RuntimeError("Desencolar: Intenta eliminar en cola vacía")
        self.__elementos.popleft()
    
    def Primero(self):
        """ Consultar el valor del primer elemento de la cola """
        if self.EsVacia():
            raise RuntimeError("Primero: Intenta consultar en cola vacía")
        return self.__elementos[0]

    def EsVacia(self)->bool:
        """ Determinar si la cola está vacía """
        return len(self.__elementos) == 0

    def __str__ (self):
        """ Generar string con el contenido de la cola """
        if self.EsVacia():
            s = "Cola Vacia"
        else:
            i = 0
            ultimo = len(self.__elementos)-1
            s = ""
            while i < ultimo:
                s += str(self.__elementos[i]) + " "
                i += 1
            s += str(self.__elementos[ultimo])
        return s
