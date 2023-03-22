from listas import linked_list, node

def eliminar_elementos_comunes(PTR1, PTR2):
    nodo_actual_PTR2 = PTR2

    while nodo_actual_PTR2 is not None:
        # Buscamos el nodo actual de PTR2 en PTR1
        nodo_actual_PTR1 = PTR1
        nodo_anterior_PTR1 = None

        while nodo_actual_PTR1 is not None and nodo_actual_PTR1.valor != nodo_actual_PTR2.valor:
            nodo_anterior_PTR1 = nodo_actual_PTR1
            nodo_actual_PTR1 = nodo_actual_PTR1.siguiente

        # Si encontramos el nodo actual de PTR2 en PTR1, lo eliminamos de PTR1
        if nodo_actual_PTR1 is not None:
            if nodo_anterior_PTR1 is None:
                PTR1 = nodo_actual_PTR1.siguiente
            else:
                nodo_anterior_PTR1.siguiente = nodo_actual_PTR1.siguiente

        nodo_actual_PTR2 = nodo_actual_PTR2.siguiente

    return PTR1

PTR1=linked_list()
PTR2=linked_list()

PTR1.add_at_front(1)
PTR1.add_at_end(2)
PTR1.add_at_end(2)
PTR1.add_at_end(3)
PTR1.add_at_end(4)
PTR1.add_at_end(5)

PTR2.add_at_front(4)
PTR2.add_at_end(2)
PTR2.add_at_end(6)
PTR2.add_at_end(8)

eliminar_elementos_comunes(PTR1,PTR2)