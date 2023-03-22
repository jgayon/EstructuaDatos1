from listas import linked_list

origen = [1,2,3,4,5,6,7,8,9]
a=linked_list()

for x in range(len(origen)):
    a.add_at_end(origen[x])

print("La lista original es esta:\n")
a.print_list()
b = int(input("Escribe la posicion del nodo que quieras eliminar (Comienza desde 0):"))

a.delete_node(origen[b])
print("Esta es la Lista despues de la eliminacion:\n")
a.print_list()