# -*- coding: utf-8 -*-
"""
Módulo auxiliar para Práctica 1 (2024).
Algoritmos de Búsqueda sobre listas.

Versión inicial no particularizada a ningún problema concreto.
Deberás realizar los cambios indicados en el guion de prácticas
y modificar este comentario. Así confirmaré si lees el material proporcionado.

@author: Jesus Albert

@date: 07/02/2024
"""
from pr1_municipio import *

def BusquedaSecuencial (v:list, #Lista con datos que dependerán de la aplicación
							x)-> (int,int):
    """ 
    Busqueda secuencial basica (sin parada).
        Args:
            v = lista con los datos
            x = elemento buscado
        Return:
            bool = encontrado (enc) = True/False
            int = pasos realizados
    """
    pasos = 0 #Contador de pasos
    enc = -1
    i = 0
    pasos += 2 #Asignaciones iniciales
    while i < len(v):
        pasos += 2 #condicion de bucle + condicion if
        if v[i].codine == x:
            enc = i
            pasos += 1 #enc = True
        i = i + 1
        pasos += 1 #i = i+1
    return enc,pasos
	
def BusquedaSecuencialParada (v:list, #Lista con datos que dependerán de la aplicación
								x)-> (int,int):
    """ 
    Busqueda secuencial con parada.
        Args:
            v = lista con los datos
            x = elemento buscado
        Return:
            bool = encontrado (enc) = True/False
            int = pasos realizados
    """
    pasos = 0 #Contador de pasos
    i = 0
    pasos += 1 #Asignación inicial
    while i < len(v) and v[i].codine != x:
        i = i + 1
        pasos += 3 #2 condiciones de bucle + asignacion
    if i == len(v):
        enc = -1
    else:
        enc = i
    pasos += 2 #if + asignación
    return enc,pasos
	
def BusquedaSecuencialCentinela (v:list, #Lista con datos que dependerán de la aplicación
									x)-> (int,int):
    """ 
    Busqueda secuencial con centinela.
        Args:
            v = lista con los datos
            x = elemento buscado
        Return:
            bool = encontrado (enc) = True/False
            int = pasos realizados
    """
    pasos = 0 #Contador de pasos
    temp_municipio = Municipio()  # Crear un Municipio temporal con el código buscado
    temp_municipio.codine = x
    v.append(temp_municipio)
    i = 0
    pasos += 2 #Asignaciones iniciales    
    while v[i].codine != x:
        i = i + 1
        pasos += 2 #condicion bucle + asignacion
    if i == len(v)-1:
        enc = -1
    else:
        enc = i
    pasos += 2 #if + asignación
    v.pop()
    pasos += 1 #pop
    return enc,pasos

def BusquedaBinaria (v:list, #Lista con datos que dependerán de la aplicación
						x)-> (int,int):
    """ 
    Busqueda binaria en una lista ordenada.
        Args:
            v = lista con los datos
            x = elemento buscado
        Return:
            bool = encontrado (enc) = True/False
            int = pasos realizados
    """
    pasos = 0 #Contador de pasos    
    izq = 0
    der = len(v) - 1
    cen = (izq + der) // 2
    pasos += 3 #Asignaciones iniciales    
    while izq <= der and v[cen].codine != x:
        if x < v[cen].codine:
            der = cen - 1
        else:
            izq = cen + 1
        cen = (izq + der) // 2
        pasos += 5 #3 condiciones + 2 asignaciones
    if izq > der:
        enc = -1
    else:
        enc = cen
    pasos += 2 #if + asignación        
    return enc,pasos
