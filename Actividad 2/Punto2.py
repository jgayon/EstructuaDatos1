from listas import node


 
def elementos_diferentes(lista):
   # Crear un conjunto vacío para almacenar los elementos únicos
    elementos_unicos = set() 
    elementos_repetidos = {}
    # Recorrer la lista enlazada
    node_actual = lista
    while node_actual is not None:
        # Si el valor del nodo actual no está en el conjunto de elementos únicos, agregarlo
        if node_actual.valor not in elementos_unicos: 
            elementos_unicos.add(node_actual.valor)
        # Si el valor del nodo actual ya está en el conjunto de elementos únicos, agregarlo a la lista de elementos repetidos
        else:
            if node_actual.valor in elementos_repetidos: 
                elementos_repetidos[node_actual.valor] += 1
            else:
                elementos_repetidos[node_actual.valor] = 1
        
        node_actual = node_actual.siguiente
   
    print("Número total de elementos diferentes:", len(elementos_unicos))
   
    for elemento, repeticiones in elementos_repetidos.items():
        print("Elementos que se repiten: ")
        print(f"{elemento} (frecuencia: {repeticiones})")

node1 = Node(5)
node2 = Node(9)
node3 = Node(8)
node4 = Node(1)
node5 = Node(5)
nodo1.siguiente = node2
nodo2.siguiente = node3
nodo3.siguiente = node4
nodo4.siguiente = node5
lista_enlazada = node1

elementos_diferentes(lista_enlazada)


