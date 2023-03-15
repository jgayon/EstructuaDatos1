from listas import linked_list, node

#Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo. 
#Entonces se debe imprimir el vector (sólo los elementos introducidos).

m= linked_list()
entrada = int(input("Ingresa el numero: "))

if entrada < 0:
    print("La lista es:\n")
    m.print_list()
else:
    m.add_at_front(entrada)
    sw = 0

    while sw == 0:
        entrada = int(input("Ingresa el numero: "))
        if entrada < 0:
            m.print_list()
            sw=1
        else:
            m.add_at_end(entrada)

