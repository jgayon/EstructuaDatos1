from listas import node


 
def elementos_diferentes(lista):
   
    elementos_unicos = set() # Crear un conjunto vacío para almacenar los elementos únicos
    elementos_repetidos = {}
    # Recorrer la lista enlazada
    nodo_actual = lista
    while nodo_actual is not None:
        
        if nodo_actual.valor not in elementos_unicos: # Si el valor del nodo actual no está en el conjunto de elementos únicos, agregarlo
            elementos_unicos.add(nodo_actual.valor)
        
        else:
            if nodo_actual.valor in elementos_repetidos: # Si el valor del nodo actual ya está en el conjunto de elementos únicos, agregarlo a la lista de elementos repetidos
                elementos_repetidos[nodo_actual.valor] += 1
            else:
                elementos_repetidos[nodo_actual.valor] = 1
        
        nodo_actual = nodo_actual.siguiente
   
    print("Número total de elementos diferentes:", len(elementos_unicos))
   
    for elemento, repeticiones in elementos_repetidos.items():
        print("Elementos que se repiten: ")
        print(f"{elemento} (frecuencia: {repeticiones})")

nodo1 = Nodo(5)
nodo2 = Nodo(9)
nodo3 = Nodo(8)
nodo4 = Nodo(1)
nodo5 = Nodo(5)
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nodo4.siguiente = nodo5
lista_enlazada = nodo1

elementos_diferentes(lista_enlazada)


