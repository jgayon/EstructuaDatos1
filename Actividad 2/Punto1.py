from listas import linked_list, node

def eliminarcomun(list1,list2):
    pass

lista1=[1,2,3,4,5,6,7,8,9]
lista2=[11,2,44,5,21,35,6,1,10]

PTR1=linked_list()
PTR2=linked_list()
list1len=len(lista1)
for x in range(list1len):
    PTR1.add_at_end(lista1[x])
print("La lista PTR1 original es:\n")
PTR1.print_list()
for x in range(len(lista2)):
    PTR2.add_at_end(lista2[x])
print("La lista PTR2 es:\n")
PTR2.print_list()
for x in range(len(lista1)):
    
    for y in range(len(lista2)):
        if (lista1[x] == lista2[y]):
            PTR1.delete_node(lista1[x])
print("La lista PTR1 actualizada es:\n")
PTR1.print_list()