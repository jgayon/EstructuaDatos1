from listas import linked_list
def count_unique_elements(linked_list):
    unique_elements = set()
    current_node = linked_list.head
    while current_node is not None:
        unique_elements.add(current_node.value)
        current_node = current_node.next
    return len(unique_elements)

num_unique_elements = count_unique_elements(linked_list)
print("El número total de elementos diferentes en la lista enlazada es:", num_unique_elements)

