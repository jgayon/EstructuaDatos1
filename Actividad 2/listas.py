# Creamos la clase node
class node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

# Creamos la clase linked_list
class linked_list: 
    def __init__(self):
        self.head = None
    
    # Método para agregar elementos en el frente de la linked list
    def add_at_front(self, data):
        self.head = node(data=data, next=self.head)  

    # Método para verificar si la estructura de datos esta vacia
    def is_empty(self):
        return self.head == None

    # Método para agregar elementos al final de la linked list
    def add_at_end(self, data):
        if not self.head:
            self.head = node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data=data)
    
    # Método para eleminar nodos
    def delete_node(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    # Método para obtener el ultimo nodo
    def get_last_node(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp.data

    # Método para imprimir la lista de nodos
    def print_list( self ):
        node = self.head
        while node != None:
            print(node.data, end =" => ")
            node = node.next
    #Invertir lista
    def invertir_lista(lista):
        prev = None
        actual = lista.head
        while actual is not None:
            siguiente = actual.next
            actual.next = prev
            prev = actual
            actual = siguiente
        lista.head = prev
    
    #contar elementos
    def contar_elementos_unicos(lista):
        elementos_unicos = set()
        nodo_actual = lista.data
    
        while nodo_actual is not None:
            elementos_unicos.add(nodo_actual.value)
            nodo_actual = nodo_actual.next
    
        return len(elementos_unicos)


