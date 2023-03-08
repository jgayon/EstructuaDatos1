class Nodo:
    def __init__(self, data = None, next=None) -> None:
        self.data = data
        self.next = next

class ListaEnlazada:
    def __init__(self) -> None:
        self.head = None
    
    def insert (self, new_node):
        if self.head:
			## getting the last node
			last_node = self.head
			while last_node != None:
				last_node = last_node.next

			## assigning the new node to the next pointer of last node
			last_node.next = new_node

		else:
			## head is empty
			## assigning the node to head
			self.head = new_node