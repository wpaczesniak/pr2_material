# -*- coding: utf-8 -*-
"""
Módulo auxiliar para Práctica 1 (2024).
Definición de un registro de Municipios.
Incluye dos funciones auxiliares:
    una para mostrar la información por pantalla y
    otra para asignar los datos a un municipio

Este archivo no requiere ninguna modificación.

@author: Jesus Albert

@date: 06/02/2024
"""

class Municipio:
    """
    Registro para representar datos de 1 municipio.
    """
    def __init__(self):
        self.codine = str() #Código INE del municipio
        self.nombre = str() #Nombre del municipio
        self.poblacion = list() #datos de poblacion desde 1998 a 2022
        #[0] = 2022, [1]=2021, ...
    
def MostrarMunicipio(m:Municipio):
    """
    Mostrar en pantalla los datos de un municipio
    
    Parameters
    ----------
    m : Municipio
        El municipio del que se muestra la informacion.

    Returns
    -------
    None.

    """
    sep = " "*4
    print("*** Datos del municipio: ")
    print(sep + "- Codine: " + m.codine)
    print(sep + "- Nombre: " + m.nombre)
    print(sep + "- Poblacion: ")
    inicio = 2022 #
    for i in range(len(m.poblacion)):
        print(sep*2 + str(inicio-i) + ": " + m.poblacion[i] + " habitantes")
    return

def GenerarMunicipio(c:str, n:str, p:list)->Municipio:
    """
    Generar un Municipio con sus datos

    Parameters
    ----------
    c : str
        Código INE del municipio.
    n : str
        Nombre del municipio.
    p : list
        Lista de datos censales por año.

    Returns
    -------
    Municipio
        El municipio generado.

    """
    m = Municipio()
    m.codine = c #Código
    m.nombre = n #Nombre
    m.poblacion = p #Datos de población
    return m
