from listas import node

def agragar_negativo(node, value):
    nuevo_nodo = Node(value)
    nuevo_nodo.next = node
    return nuevo_nodo

def agregar_positivo(node, value):
    nuevo_nodo = Node(value)
    nuevo_nodo.next = node.next
    node.next = nuevo_nodo

def eliminar_nodo(prev_node, node):
    prev_node.next = node.next

def modificar_lista(head):
    nodo_actual = head
    prev = None
    while nodo_actual:
        if nodo_actual.data < 0:
            nuevo_nodo = Node(-1000)
            if prev is None:
                head = agragar_negativo(nodo_actual, -1000)
            else:
                agragar_negativo(nodo_actual, -1000)
            nodo_actual = nuevo_nodo.next
        elif nodo_actual.data > 0:
            if nodo_actual.next is None:
                agregar_positivo(nodo_actual, 1000)
                nodo_actual = nodo_actual.next
            else:
                agregar_positivo(nodo_actual, 1000)
                nodo_actual = nodo_actual.next.next
        else:
            if prev is None:
                head = nodo_actual.next
                nodo_actual = head
            else:
                eliminar_nodo(prev, nodo_actual)
                nodo_actual = prev.next
        prev = nodo_actual
        if nodo_actual:
            nodo_actual = nodo_actual.next
    return head

head = Node(-3)
head.next = Node(5)
head.next.next = Node(0)


print("Lista original:")
nodo_actual = head
while nodo_actual:
    print(nodo_actual.data, end=" ")
    nodo_actual = nodo_actual.next
print()


head = modificar_lista(head)


print("Lista modificada:")
nodo_actual = head
while nodo_actual:
    print(nodo_actual.data, end=" ")
    nodo_actual = nodo_actual.next
print()

