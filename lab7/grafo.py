# -*- coding: utf-8 -*-
"""
Clase Grafo
Grafo con listas de adyacencia y diccionarios 
@author Jesús Albert
@date 09/05/2023
"""
from clase_cola import Cola

class Grafo: 
    """ --------------------------- """
    """ --- Clase Nodo, privada --- """
    """ --------------------------- """

    class __Nodo:
        """Nodo = info"""
        def __init__ (self,info=None):
            self.info = info  

        def __str__(self)->str:
            """ Conversión str """
            return str(self.info)

    """ ---------------------------- """
    """ --- Operaciones de GRAFO --- """
    """ ---------------------------- """
                   
    def __init__ (self, nnodos:int):
        """
        Construir un grafo vacío con nndos
        Para cada nodo se crea un diccionario de arcos
        
        Parameters
        ----------
        nnodos : int
            numero de nodos.

        Returns
        -------
        None.

        """
        self.__nodos = [ Grafo.__Nodo() for x in range(nnodos) ]
        self.__arcos = [ {} for x in range(nnodos) ]
        
    """ ----------------------------------- """
    """ --- Operaciones sobre los Arcos --- """
    """ ----------------------------------- """

    def AsignarArco(self, origen:int, destino:int, peso=1):
        """
        Asignar un peso al arco 'origen'-->'destino' 

        Parameters
        ----------
        origen : int
            indice del nodo origen del arco.
        destino : int
            indice del nodo destino del arco.
        peso : int
            peso del arco. Valor por deefecto, 1

        Raises
        ------
        RuntimeError
            si origen o destino fuera del rango de los nodos del grafo.

        Returns
        -------
        None.

        """
        if (0 <= origen < len(self.__nodos)) and (0 <= destino < len(self.__nodos)):
            # si el arco existe, modificar peso
            # si el arco no existe, añadirlo
            self.__arcos[origen][destino] = peso           
        else:
            raise RuntimeError("AsignarArco: nodo no existe "+str(origen)+" "+str(destino))
            
            
    def PesoArco(self, origen:int, destino:int)->int:
        """
        Obtener el peso del arco 'origen'-->'destino' 

        Parameters
        ----------
        origen : int
            indice del nodo origen del arco.
        destino : int
            indice del nodo destino del arco.

        Raises
        ------
        RuntimeError
            si origen o destino fuera del rango de los nodos del grafo.

        Returns
        -------
        int
            peso del arco, 0 si no hay arco.

        """
        if (0 <= origen < len(self.__nodos)) and (0 <= destino < len(self.__nodos)):
            # si el arco existe, consultar peso
            # si el arco no existe, peso = 0
            if destino in self.__arcos[origen]:
                peso = self.__arcos[origen][destino]
            else:
                peso = 0         
            return peso
        else:
            raise RuntimeError("PesoArco: nodo no existe "+str(origen)+" "+str(destino))
        
    """ ------------------------------- """
    """ --- Operaciones sobre Nodos --- """
    """ ------------------------------- """
    
    def Size(self)->int:
        """
        Número de nodos del grafo 

        Returns
        -------
        int
            Número de nodos del grafo.

        """
        return len(self.__nodos)

    def AsignarInfoNodo(self,nodo:int,info:str):
        """
        Asignar información a un nodo ya existente del grafo

        Parameters
        ----------
        nodo : int
            indice del nodo al que se asigna información.
        info : str
            información asociada.

        Raises
        ------
        RuntimeError
            si nodo fuera del rango de los nodos del grafo.

        Returns
        -------
        None.

        """
        if 0 <= nodo < len(self.__nodos):
            self.__nodos[nodo] = info
            return
        else:
            raise RuntimeError("AsignarInfoNodo: nodo no existe "+str(nodo))

    def InfoNodo(self,nodo:int)->str:
        """
        Obtener la información asociada con el índice del nodo

        Parameters
        ----------
        nodo : int
            indice del nodo.

        Raises
        ------
        RuntimeError
            si nodo fuera del rango de los nodos del grafo.

        Returns
        -------
        str
            información asociada.

        """
        if 0 <= nodo < len(self.__nodos):
            return self.__nodos[nodo]
        else:
            raise RuntimeError("InfoNodo: nodo no existe "+str(nodo))

    def IndiceNodo(self,info:str)->int:
        """
        Obtiene el índice del nodo correspondiente a la información del nodo

        Parameters
        ----------
        info : str
            información que identifica al nodo, componente 0 de la info.

        Raises
        ------
        RuntimeError
            si info no encontrada entre los nodos del grafo.

        Returns
        -------
        int
            identificador numérico del nodo.

        """
        try:
            ind = self.__nodos.index(info)
        except:
            raise RuntimeError("IndiceNodo: info no encontrada en el grafo "+str(info))
        else:
            return ind
            
    def NodosAdyacentes(self, origen:int)->list:
        """
        Obtener la lista de nodos adyacentes a 'origen'

        Parameters
        ----------
        origen : int
            nodo origen de los arcos cuyos destinos se buscan.

        Raises
        ------
        RuntimeError
            si origen fuera del rango de los nodos del grafo.

        Returns
        -------
        list
            lista de nodos adyacentes.

        """
        if 0 <= origen < len(self.__nodos):
            res = []
            #Nodos adyacentes = todas las claves del diccionario de arcos salientes
            for k in self.__arcos[origen]:
                res.append(k)
            return res
        else:
            raise RuntimeError("NodosAdyacentes: nodo no existe "+str(origen))

    def NodosArcosIncidentes (self, destino:int)->list:
        """
        Obtener la lista de nodos con arcos que inciden en 'destino'

        Parameters
        ----------
        destino : int
            nodo destino de los arcos cuyos origenes se buscan.

        Raises
        ------
        RuntimeError
            si destino fuera del rango de los nodos del grafo.

        Returns
        -------
        list
            lista de nodos incidentes.

        """
        if 0 <= destino < len(self.__nodos):
            res = []
            #para todos los nodos
            for n in range(len(self.__nodos)):
                #Buscar destino en el diccionario de arcos de n
                if destino in self.__arcos[n]:
                    res.append(n)
            return res
        else:
            raise RuntimeError("NodosArcosIncidentes: nodo no existe "+str(destino))

    """ ---------------------------------- """
    """ --- Operaciones de Exploración --- """
    """ ---------------------------------- """

    def DFS (self, origen:int,visitados:set):
        """
        Recorrido en Profundidad (DFS) del grafo 

        Parameters
        ----------
        origen : int
            identificador del nodo origen del recorrido.
        visitados : set
            conjunto de nodos visitados [in/out].

        Raises
        ------
        RuntimeError
            si origen fuera del rango de los nodos del grafo.

        Returns
        -------
        None.

        """
        if 0 <= origen < len(self.__nodos):        
            visitados.add(origen)
            for n in self.NodosAdyacentes(origen):
                    if not n in visitados:
                        self.DFS(n,visitados)
        else:
            raise RuntimeError("DFS: origen no existe "+str(origen))

    def BFS (self, origen:int,visitados:set)->list:
        """
        Recorrido en Anchura (BFS) del grafo

        Parameters
        ----------
        origen : int
            identificador (int) del nodo origen del recorrido.
        visitados : set
            conjunto de nodos visitados [in/out].

        Raises
        ------
        RuntimeError
            si origen fuera del rango de los nodos del grafo.

        Returns
        -------
        list
            distancia a todos los nodos del grafo desde el origen, -1 si no visitado
        """
        if 0 <= origen < len(self.__nodos):        
            #Crear lista de distancias al origen, todos los nodos no visitados
            dist  = [ -1 for i in range(self.Size())]
            visitados.add(origen)
            dist[origen] = 0 #Por ser el origen, está a dist. 0 de sí mismo
            q = Cola()
            q.Encolar(origen)
            while not q.EsVacia():
                origen = q.Primero() #Nuevo origen
                q.Desencolar()
                for n in self.NodosAdyacentes(origen):
                    if n not in visitados: #No visitado
                        visitados.add(n)
                        dist[n] = dist[origen]+1 #actualizar su distancia
                        q.Encolar(n)
            return dist
        else:
            raise RuntimeError("BFS: origen no existe "+str(origen))

    def ImprimirGrafo(self):
        """
        Imprimir las listas de adyacencia del grafo

        Returns
        -------
        None.

        """
        for i in range(len(self.__nodos)):
            print("Nodo",i,"(",self.__nodos[i],"): ",end="")
            for j in self.NodosAdyacentes(i):
                print("("+str(j)+","+str(self.PesoArco(i,j))+") ", end="")
            print()
        return
            
""" -------- Fin clase Grafo --------"""

def main():
    """ Programa de test de la clase Grafo """
    #Definir la información de los nodos
    datos = [ chr(ord('A')+i) for i in range(10)]
    #Crear grafo con tantos nodos como datos
    g = Grafo (len(datos)) 
    #Asignar la información de "datos" a los nodos, que están vacíos
    for i in range(len(datos)):
        g.AsignarInfoNodo(i,datos[i])
    #Crear arcos de un nodo i a todos los nodos con identificador >=i
    for i in range(g.Size()):
        for j in range(g.Size()):
            if i <= j:
                g.AsignarArco(i,j,1);
    Test_1(g)
    Test_2(g)
    Test_3(g)
    Test_4(g)
    Test_5(g)
    
    return

""" --- Las funciones de Test --- """

def Test_1 (g:Grafo):
    #Mostrar grafo creado
    print()
    print("Test 1: Grafo con 10 nodos y arcos con índices >= nodo")
    g.ImprimirGrafo()
    print()
    input("Pulsar <Enter/Intro> para continuar...")
    print()
    
def Test_2 (g:Grafo):
    #Recorrido DFS del grafo (profundidad)
    print("Test 2: Recorrido DFS(0), nodos visitados desde 0")
    v=set()
    origen = 0
    g.DFS(origen,v)
    print("Índices de nodos visitados:",v)
    print("Información de los nodos visitados:")
    for x in v:
        print(g.InfoNodo(x)," ",end="")
    print()
    input("Pulsar <Enter/Intro> para continuar...")
    print()
    
def Test_3 (g:Grafo):
    #Recorrido BFS del grafo (anchura)
    print("Test 3: Recorrido BFS(6), nodos visitados desde 6")
    v=set()
    origen = 6
    g.BFS(origen,v)
    print("Índices de los nodos visitados:",v)
    print("Información de los nodos visitados:")
    for x in v:
        print(g.InfoNodo(x)," ",end="")
    print()
    input("Pulsar <Enter/Intro> para continuar...")
    print()
    
def Test_4 (g:Grafo):
    #Mostrar nodos adyacentes a cada nodo del grafo
    print("Test 4: Nodos Adyacentes a cada nodo:")
    for i in range(g.Size()):
        print("Nodo",i,": ",g.NodosAdyacentes(i))
    print()
    input("Pulsar <Enter/Intro> para continuar...")
    print()
    
def Test_5 (g:Grafo):
    #Mostrar nodos con arcos incidentes a cada nodo del grafo
    print("Test 5: Nodos con arcos Incidentes en cada nodo:")
    for i in range(g.Size()):
        print("Nodo",i,": ",g.NodosArcosIncidentes(i))
    print()
    
if __name__ == "__main__":
    main()