from listas import Node
def listas_semejantes (lista1, lista2):
    # Convertir las listas enlazadas a listas simples
    list1 = []
    list2 = []
    while list1:
        lista1.append(list1.data)
        list1 = list1.next
    while list2:
        lista2.append(list2.data)
        list2 = lista2.next

    # Ordenar la listas
    list1.sort()
    list2.sort()

    # Verificamos si las listas son iguales
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

lista1 = Node(2)
lista1.next = Node(6)
lista1.next.next = Node(1)
lista1.next.next.next = Node(5)

lista2 = Node(1)
lista2.next = Node(5)
lista2.next.next = Node(6)
lista2.next.next.next = Node(2)

if listas_semejantes(lista1, lista2):
    print("Son listas semejantes ")
else:
    print("No son listas semejantes")
