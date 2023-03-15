from listas import linked_list, node;
import random

#Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) 
#y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

b = linked_list()
cuadrado = []
cubo = []
num=random.randint(1,10)
b.add_at_front(num)
cuadrado.append(num**2)
cubo.append(num**3)
for x in range(9):
    num=random.randint(1,10)
    b.add_at_end(num)
    cuadrado.append(num**2)
    cubo.append(num**3)
print("Lista\n")
b.print_list()
print("\nLista al Cuadrado\n")
print(cuadrado)
print("\nLista al Cubo\n")
print(cubo)