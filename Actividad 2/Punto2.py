from listas import node


 
def elementos_diferentes(lista):
   
    elementos_unicos = set() 
    elementos_repetidos = {}
   
    node_actual = lista
    while node_actual is not None:
        
        if node_actual.valor not in elementos_unicos: 
            elementos_unicos.add(node_actual.valor)
        
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


