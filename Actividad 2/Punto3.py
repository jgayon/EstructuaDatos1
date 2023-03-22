from listas import linked_list

a = linked_list()
a.add_at_front(1)
a.add_at_end(2)
a.add_at_end(3)
a.add_at_end(4)
a.add_at_end(5)
print("La lista original es:")
a.print_list()
print("\nla lista invertida es: ")
a.invertir_lista()
a.print_list()