# -*- coding: utf-8 -*-
"""
Práctica 5: 
Clase Árbol Binario de Búsqueda (ABB)

@author: Jesus Albert
@date: 16/04/2024
"""

"""Clase Árbol Binario de Búsqueda"""
class ABB:

    """Clase ABB.ParDato:
    Tipo de información almacenada en cada nodo del árbol.
    El tipo y sus atributos son públicos para todas las aplicaciones."""
    class ParDato:
        def __init__(self,clave,valor):
            self.clave = clave #clave que identifica a los datos
            self.valor = valor #valor completo de los datos
            
        def __str__ (self)->str:
            s = str(self.clave) + " --> " 
            s += str(self.valor) + "\n"
            return s
        
            
    """ Clase ABB.__Nodo:
    Clase privada que representa los componentes del árbol ABB.
    """
    class __Nodo:
        def __init__ (self, dato, #:ABB.ParDato
                      hizq, #:ABB.__Nodo
                      hder #:ABB.__Nodo
                      ):
            """
            Constructor: 
                Crear un nuevo nodo con dato, hijo izq. e hijo der.

            Parameters
            ----------
            dato : ABB.ParDato
                par (clave,valor) almacenado en el nodo
            hizq: ABB.__Nodo
                hijo izquierdo (es un Nodo)
            hder: ABB.__Nodo
                hijo derecho (es un Nodo)

            Returns
            -------
            None.

            """
            self.dato = dato
            self.hizq = hizq
            self.hder = hder
        
        def SetDato (self, pdato #:ABB.ParDato
                     ):
            """
            Modificar el dato del nodo, de tipo ABB.ParDato 

            Parameters
            ----------
            pdato: ABB.ParDato
                dato del nodo, es ParDato

            Returns
            -------
            None.

            """           
            self.dato = pdato
            
        def SetIzq (self, hijo #:ABB.__Nodo
                    ):
            """
            Modificar el hijo izquierdo, de tipo ABB.__Nodo 

            Parameters
            ----------
            pdato: ABB.__Nodo
                hijo izquierdo del nodo, es __Nodo

            Returns
            -------
            None.

            """           
            self.hizq = hijo
            
        def SetDer (self, hijo #:ABB.__Nodo
                    ):
            """
            Modificar el hijo derecho, de tipo ABB.__Nodo 

            Parameters
            ----------
            pdato: ABB.__Nodo
                hijo derecho del nodo, es __Nodo

            Returns
            -------
            None.

            """           
            self.hder = hijo            

        def GetDato (self): #-> ABB.ParDato
            """ Obtener la información del nodo, de tipo ABB.ParDato """
            return self.dato
        
        def GetIzq (self): #-> ABB.__Nodo
            """ Obtener el nodo izquierdo, de tipo ABB.__Nodo """
            return self.hizq
        
        def GetDer (self): #-> ABB.__Nodo
            """ Obtener el nodo derecho, de tipo ABB.__Nodo """
            return self.hder
    
    """ -------- Operaciones de la clase ABB -------- """
    
    def __init__ (self, dato = None, izq = None, der = None):
        """
        Constructor del árbol ABB

        Parameters
        ----------
        dato : ABB.ParDato, optional
            Dato de la raiz del árbol. The default is None.
        izq : ABB, optional
            Subárbol izquierdo. The default is None.
        der : TYPE, optional
            Subárbol derecho. The default is None.

        Returns
        -------
        None.

        """
        """ Creación del nodo raiz """
        if dato == None: # si no hay dato, árbol vacío
            self.__raiz = None
        else:
            if izq == None:
                izq = ABB()
            if der == None:
                der = ABB()
            self.__raiz = ABB.__Nodo(dato,izq.__raiz,der.__raiz)
    
    def EsVacio (self)->bool:
        """
        Determinar si el árbol está vacío

        Returns
        -------
        bool
            True = árbol vacío, False = no vacío, hay elementos

        """
        return self.__raiz == None
    
    def Buscar(self,clave)->(bool #,valor asociado a la clave
                             ):
        """
        Buscar una clave en el árbol

        Parameters
        ----------
        clave 
            clave a buscar

        Returns
        -------
        (bool,valor)
            True/False (encontrado), valor asociado con la clave

        """
        enc = False
        valor = None
        nodo = self.__raiz
        while nodo != None and not enc:
            if clave < nodo.dato.clave:
                nodo = nodo.GetIzq()
            elif clave > nodo.dato.clave:
                nodo = nodo.GetDer()
            else:
                enc = True
                valor = nodo.GetDato().valor
        return enc,valor

    def Insertar(self,clave,valor)->bool:
        """
        Insertar una nueva pareja (clave,valor) en el árbol

        Parameters
        ----------
        clave 
            clave identificativa
        valor 
            valor asociado

        Returns
        -------
        bool
            True= insertado, False=no insertado, la clave ya estaba en el árbol

        """
        enc = False
        if self.__raiz == None:
            x = ABB.ParDato(clave,valor)
            self.__raiz = ABB.__Nodo(x,None,None)
        else:
            nodo = self.__raiz
            fin = False
            while not fin:
                if clave < nodo.GetDato().clave:
                    if nodo.GetIzq() != None:
                        nodo = nodo.GetIzq()
                    else:
                        x = ABB.ParDato(clave,valor)
                        nodo.SetIzq(ABB.__Nodo(x,None,None))
                        fin = True
                elif clave > nodo.GetDato().clave:
                    if nodo.GetDer() != None:
                        nodo = nodo.GetDer()
                    else:
                        x = ABB.ParDato(clave,valor)
                        nodo.SetDer(ABB.__Nodo(x,None,None))
                        fin = True
                else:
                    enc = True
                    fin = True
        return not enc
    
    def Modificar(self,clave,valor)->bool:
        """
        Modificar el valor asociado con una clave existente en el árbol

        Parameters
        ----------
        clave 
            clave identificativa
        valor 
            nuevo valor asociado

        Returns
        -------
        bool
            True= clave encontrada y valor modificado, 
            False= clave no encontrada

        """
        b = False
        nodo = self.__raiz
        while nodo != None and not b:
            if clave < nodo.info.clave:
                nodo = nodo.GetIzq()
            elif clave > nodo.info.clave:
                nodo = nodo.GetDer()
            else:
                b = True
                nodo.SetInfo(ABB.ParDato(clave,valor))
        return b
 
    def SubarbIzq (self): #-> ABB
        """
        Obtener el ABB cuya raiz es el hijo izquierdo de la raiz

        Raises
        ------
        RuntimeError
            cuando el árbol está vacío

        Returns
        -------
        a : ABB
            subárbol izquierdo

        """
        if self.EsVacio():
            raise RuntimeError ("Error: Intento de acceso a hijo izquierdo de un árbol vacío.")
        else:
            a = ABB()
            a.__raiz = self.__raiz.GetIzq()
            return a

    def SubarbDer (self): #-> ABB
        """
        Obtener el ABB cuya raiz es el hijo derecho de la raiz

        Raises
        ------
        RuntimeError
            cuando el árbol está vacío

        Returns
        -------
        a : ABB
            subárbol derecho

        """
        if self.EsVacio():
            raise RuntimeError ("Error: Intento de acceso a hijo derecho de un árbol vacío.")
        else:
            a = ABB()
            a.__raiz = self.__raiz.GetDer()
            return a
    
    def Raiz (self): #-> ABB.ParDato
        """
        Obtener la información en la raíz del ABB

        Raises
        ------
        RuntimeError
            cuando el árbol está vacío

        Returns
        -------
        ABB.ParDato
            par (clave,valor) en la raíz del árbol

        """        
        if self.EsVacio():
            raise RuntimeError ("Error: Intento de acceso hijo derecho de un árbol vacío.")
        else:
            return self.__raiz.GetDato()
        
    def ImprimirArbol(self, txt="", prof=0):
        """
        Imprimir con formato el árbol

        Parameters
        ----------
        f : TextIO
            archivo de texto para guardar la salida, 
            debe de estar correctamente abierto para escritura "w"        
        txt : str, optional
            texto informativo que precede a la información de cada nodo. 
            The default is "".
        prof : int, optional
            profundidad del nodo. The default is 0.

        Returns
        -------
        None.

        """
        if not self.EsVacio():
            # f.write("   "*prof + txt + str(self.Raiz()) + "\n")
            print("   "*prof + txt + str(self.Raiz()))           
            self.SubarbIzq().ImprimirArbol("[IZQ] ",prof+1)
            self.SubarbDer().ImprimirArbol("[DER] ",prof+1)
def main():
    print(__doc__)
    a = ABB()
    help(a)

if __name__ == "__main__":
    main()