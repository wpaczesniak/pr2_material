# -*- coding: utf-8 -*-
"""Práctica 3 (2024). Test Clase Aeropuerto

Este archivo no se debe modificar,
se debe ejecutar para comprobar el correcto funcionamiento
de la clase Aeropuerto

@author: Jesus Albert
@date: 05/03/2024
"""

from pr3_aeropuerto import Aeropuerto

def AsignarValores(a:Aeropuerto,s:str):
    """
    Asignar los datos de una cadena s al aeropuerto a

    Parameters
    ----------
    a : Aeropuerto
    s : str
        cadena con los campos separados por ";"

    Returns
    -------
    None.

    """
    datos = s.split(";")
    tmp = Aeropuerto()
    try:
        tmp.SetIATA(datos[4])
        tmp.SetICAO(datos[5])
        tmp.SetDST(datos[10])
    except RuntimeError as e:
        raise e
    else:
        a.SetID(int(datos[0]))
        a.SetNombre(datos[1])
        a.SetCiudad(datos[2])
        a.SetPais(datos[3])
        a.SetIATA(datos[4])
        a.SetICAO(datos[5])
        a.SetLatitud(float(datos[6]))
        a.SetLongitud(float(datos[7]))
        a.SetAltitud(float(datos[8]))
        a.SetTimezone(float(datos[9]))
        a.SetDST(datos[10])
    return
    
def main():
    """ Programa de Test de la clase Aeropuerto
    Este programa debe proporcionar los resultados indicados en cada test
    una vez que se hayan completado correctamente todas las operaciones y
    se hayan incluido las comprobaciones pertinentes.
    """
    print(__doc__)
    print("*"*50)
    print(main.__doc__)
    print("*"*50)

    a = Aeropuerto()
    
    print("TEST 1. Aeropuerto por defecto:")
    print("\n",a,"\n")

    print("*"*50)
    print("TEST 2. Aeropuerto con valores correctos asignados:")
    cadena_1 = "1;Goroka Airport;Goroka;Papua New Guinea;GKA;AYGA;-6.081689835;145.3919983;5282;10;U"
    AsignarValores(a,cadena_1)
    print("\n",a,"\n")
    
    print("*"*50)
    print("TEST 3. Aeropuerto con valores INcorrectos asignados (NO debe cambiar nada):")
    cadena_2 = "2;Madang Airport;Madang;Papua New Guinea;MA;AYM;-5.207079887;145.7890015;20;10;X"
    try:
        AsignarValores(a,cadena_2)
    except RuntimeError as e:
        print("\tCorrecto: Detectada Excepción al asignar valores")
        print("\t"+str(e))
    else:
        print("\tError: No se ha lanzado excepción")
    print("\n",a,"\n")
    
    print("*"*50)
    print("TEST 4. Mostrar valores del aeropuerto usando las operaciones Get:")
    print()
    print("\tId: ",a.GetID())
    print("\tNombre: ",a.GetNombre())
    print("\tCiudad: ",a.GetCiudad())
    print("\tPais: ",a.GetPais())
    print("\tIATA: ",a.GetIATA())
    print("\tICAO: ",a.GetICAO())
    print("\tLatitud: ",a.GetLatitud())
    print("\tLongitud: ",a.GetLongitud())
    print("\tAltitud: ",a.GetAltitud())
    print("\tTimezone: ",a.GetTimezone())
    print("\tDST: ",a.GetDST())
    print("*"*50)
    print("FIN")
    return
    
if __name__ == '__main__':
    main()