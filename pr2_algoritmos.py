# -*- coding: utf-8 -*-
"""
Módulo auxiliar para Práctica 2 (2024).
Algoritmos de Ordenación de listas.

Versión en la que se incluye en cada algoritmo la función de comparación
de elementos a utilizar. Esto permite generalizar a diferentes criterios
de comparación.

@author: Jesus Albert

@date: 17/02/2024
"""

def OrdSeleccion (v:list, menor)->int:
    """
    Algoritmo de ordenación por Selección
    Parameters
    ----------
    v : list
        Lista con los datos.
    menor : nombre de funcion
        Función utilizada para comparar si elemento de la lista es menor que otro.
        Se debe pasar solo el nombre de la función, sin argumentos.
        
    Returns
    -------
    int = pasos realizados sobre elementos de la lista
    """
    pasos = 0 #Contador de pasos    
    n = len(v)
    for i in range(n-1): #para todas las posiciones
        pos_min = i #primer minimo
        for j in range(i+1,n):
            pasos += 1
            if menor(v[j],v[pos_min]): #v[j] < v[pos_min]:
                pos_min = j #nuevo minimo
        v[i],v[pos_min] = v[pos_min],v[i]
        pasos += 1
    return pasos

def OrdQuicksort (v:list, menor)->int:
    """
    Algoritmo de ordenación Quicksort
    Parameters
    ----------
    v : list
        Lista con los datos.
    menor : nombre de funcion
        Función utilizada para comparar si elemento de la lista es menor que otro.
        Se debe pasar solo el nombre de la función, sin argumentos.

    Returns
    -------
    int = pasos realizados sobre elementos de la lista
    """
    #realizar la particion del toda la lista
    return Particion(v, 0, len(v)-1, menor)    

def Particion (v:list, izq:int, der:int, menor)->int:
    """
    Función de partición del algoritmo Quicksort
    Parameters
    ----------
    v : list
        Lista con los datos.
    izq : int
        Límite inferior de la zona de partición.
    der : int
        Límite superior de la zona de partición.
    menor : nombre de funcion
        Función utilizada para comparar si elemento de la lista es menor que otro.
        Se debe pasar solo el nombre de la función, sin argumentos.

    Returns
    -------
    int = pasos realizados sobre elementos de la lista
    """
    pasos = 0 #Contador de pasos    
    piv = v[ (izq + der)//2 ]
    i = izq
    j = der
    while i <= j:
        while menor(v[i],piv): #v[i] < piv = parar si mal ubicado a la izquierda
            pasos += 1
            i += 1
        while not menor(v[j],piv) and v[j] != piv: #v[j] > piv = parar si mal ubicado a la derecha
            pasos += 1
            j -= 1
        if i < j: #intercambiar mal ubicados
            v[i],v[j] = v[j],v[i]
            pasos += 1
            i += 1
            j -= 1
        elif i == j: #forzar finalizar particion
            i += 1
            j -= 1
    
    if izq < j: #continuar con particion izquierda
        pasos += Particion(v,izq,j,menor)
    if i < der: #continuar con particion derecha
        pasos += Particion(v,i,der,menor)
    return pasos
