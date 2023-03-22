from listas import linked_list
origen=[-4,-3,-2,-1,0,1,2,3,4]
a=linked_list()

for x in range(len(origen)):
    a.add_at_end(origen[x])
print("La lista original es:\n")
a.print_list()

PTR1=linked_list()
PTR2=linked_list()

for x in range(len(origen)):
    if origen[x] <0:
        PTR2.add_at_end(origen[x])
    elif origen[x] == 0:
        a.delete_node(0)
    elif origen[x] > 0:
        PTR1.add_at_end(origen[x])

print("\nLa lista PTR1 es:\n")
PTR1.print_list()
print("\nLa lista PTR2 es:\n")
PTR2.print_list()
print("\nLa lista original sin 0 es:\n")
a.print_list()