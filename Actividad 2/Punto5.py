def contar_elementos(lista):
    L1 = []  # lista para almacenar los elementos sin repetir
    L2 = []  # lista para almacenar la cantidad de repeticiones de cada elemento
    for elemento in lista:
        if elemento not in L1:  # si el elemento no está en la lista L1
            L1.append(elemento)  # lo agregamos a L1
            L2.append(1)  # inicializamos la cantidad de repeticiones en 1
        else:  # si el elemento ya está en la lista L1
            indice = L1.index(elemento)  # buscamos su índice en L1
            L2[indice] += 1  # incrementamos la cantidad de repeticiones en L2
    return L1, L2

lista = [1, 2, 3, 2, 4, 1, 5, 4, 4, 1]
L1, L2 = contar_elementos(lista)
print("Elementos:", L1)
print("Repeticiones:", L2)