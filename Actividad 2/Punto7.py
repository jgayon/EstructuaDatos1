from listas import Node

def lista_comun(ptr1, ptr2):
    ptr3 = None
    while ptr1 and ptr2:
        if ptr1.data == ptr2.data:
            nuevo_nodo = Node(ptr1.data)
            nuevo_nodo.next = ptr3
            ptr3 = nuevo_nodo
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        elif ptr1.data < ptr2.data:
            ptr1 = ptr1.next
        else:
            ptr2 = ptr2.next
    return ptr3

    ptr3.sort(reverse=True) #método para ordenar las listas de forma descendente


ptr1 = Node(1)
ptr1.next = Node(3)
ptr1.next.next = Node(5)
ptr1.next.next.next = Node(7)
ptr1.next.next.next.next = Node(10)
ptr1.next.next.next.next.next = Node(11)

ptr2 = Node(3)
ptr2.next = Node(4)
ptr2.next.next = Node(5)
ptr2.next.next.next = Node(8)
ptr2.next.next.next.next = Node(10)
ptr2.next.next.next.next.next = Node(11)

ptr3 = lista_comun(ptr1, ptr2)



while ptr3:
    print(ptr3.data)
    ptr3 = ptr3.next
