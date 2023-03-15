from listas import linked_list
import random

#Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), 
#y posterior ordene los elementos de menor a mayor.

original=[]

p=linked_list()
f=linked_list()

for x in range(9):
    original.append(random.randint(0,100))

p.add_at_front(original[0])
for x in range(1,9):
    p.add_at_end(original[x])

original.sort()

f.add_at_front(original[0])
for x in range(1,9):
    f.add_at_end(original[x])
print("Lista Original:\n")
p.print_list()
print("\nLista Ordenada:\n")
f.print_list()