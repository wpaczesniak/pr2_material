# -*- coding: utf-8 -*-
"""
Módulo auxiliar para Práctica 2 (2024).

Clase Municipio

Este archivo no requiere ninguna modificación.

@author: Jesus Albert

@date: 17/02/2024
"""

class Municipio:
    """
    Clase para representar datos de 1 municipio
    Resumen de operaciones públicas:
        - Constructor
        - SetLinea(self,s:str): Poner datos a partir de una linea de texto csv
        - SetDatos(self,c:str, n:str, p:list): Asignar todos los datos
        - GetCodine(self): Consultar el codigo INE del municipio
        - GetNombre(self): Consultar el nombre del municipio
        - GetPoblacion(self,a:int): Consultar los habitantes del municipio en un año
        - str(self): Convertir en string el municipio
    """
    INICIO = 2022 #Cte. que establece año del primer elemento de la lista de población

    def __init__(self):
        """
        Constructor de la clase

        Returns
        -------
        None.

        """
        self.__codine = "<sin codigo>" #Código INE del municipio
        self.__nombre = "<sin nombre>" #Nombre del municipio
        self.__poblacion = list() #datos de poblacion desde 1998 a 2022
        #[0] = 2022, [1]=2021, ...
        return

    def SetLinea(self,s:str):
        """
        Establecer datos del municipio (self) a partir de una linea de texto csv

        Parameters
        ----------
            s = texto csv a procesar
            
        Returns
        -------
        None.
        """       
        s = s.rstrip("\n") #elimina \n si lo tuviera
        l = list()
        l = s.split(";")
        #asignar los datos de la linea
        self.SetDatos(l[0],l[1],l[2:])
        return

    def SetDatos(self, c:str, n:str, p:list):
        """
        Asignar los datos del Municipio (self)

        Parameters
        ----------
        c : str
            Codigo INE del municipio.
        n : str
            Nombre del municipio.
        p : list
            Lista de datos censales por año.

        Returns
        -------
        None.
        """
        self.__codine = c #Código
        self.__nombre = n #Nombre
        self.__poblacion = p #Datos de población
        return

    def GetCodine(self)->str:
        """
        Consultar el codigo INE del municipio

        Returns
        -------
        str
            Codigo INE

        """
        return self.__codine
    
    def GetNombre(self)->str:
        """
        Consultar el nombre del municipio

        Returns
        -------
        str
            Nombre

        """
        return self.__nombre
    
    def GetPoblacion(self,a:int)->int:
        """
        Consultar los habitantes del municipio en un año concreto

        Parameters
        ----------
        a : int
            año
            Error si a no está en el rango de años registrados

        Returns
        -------
        int
            Número de habitantes 

        """
        ultimo = Municipio.INICIO #último año de la serie, primero de la lista
        primero = ultimo - len(self.__poblacion)-1 #primer año de la serie, último de la lista
        if primero <= a <= ultimo: #determinar si hay datos para el año a
            x = self.__poblacion[ultimo-a]
            if x == "x" or x == '""': #puede haber datos no registrados en el archivo
                h = 0
            else:
                h = int(x)
        else:
            print("Municipio.GetPoblacion(): Error año", a)
            h = 0
        return h

    def __str__(self)->str:
        """
        Convertir en string la informacion del municipio
        Returns
        -------
        str
            string con la informacion del municipio
        """
        s = self.__codine + " "
        s += self.__nombre + " "
        s += str(self.__poblacion) + "\n"
        return s

