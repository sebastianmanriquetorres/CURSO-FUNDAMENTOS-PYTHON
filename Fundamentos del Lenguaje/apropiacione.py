def agregar_una_vez(lista, el):
    try:
        if el in lista:
            raise ValueError(f"Error: el elemento '{el}' ya se encuentra en la lista.")
        else:
            lista.append(el)
    except ValueError as e:
        print(e)

mi_lista = [1, 2, 3]

print("Lista actual:", mi_lista)

entrada = input("Ingresa un elemento para agregar a la lista: ")

try:
    entrada = int(entrada)
except ValueError:
    pass  

agregar_una_vez(mi_lista, entrada)

print("Lista actualizada:", mi_lista)