from listas import node

def count_different_elements(head):
    if not head:
        return 0

    current_node = head
    different_elements = set([current_node.val])

    while current_node.next:
        current_node = current_node.next
        if current_node.val not in different_elements:
            different_elements.add(current_node.val)

    return len(different_elements)

# Ejemplo de lista enlazada
head = Node(3)
head.next = Node(4)
head.next.next = Node(5)
head.next.next.next = Node(4)
head.next.next.next.next = Node(6)
head.next.next.next.next.next = Node(3)
head.next.next.next.next.next.next = Node(2)
head.next.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next.next = Node(5)

# Contar los elementos diferentes en la lista
num_different = count_different_elements(head)
print("El número total de elementos diferentes en la lista es:", num_different)

# Imprimir los elementos diferentes
current_node = head
different_elements = set([current_node.val])
while current_node.next:
    current_node = current_node.next
    if current_node.val not in different_elements:
        different_elements.add(current_node.val)

print("Los elementos diferentes en la lista son:", different_elements)


