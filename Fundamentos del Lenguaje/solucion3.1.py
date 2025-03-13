# Pedir al usuario la cantidad de elementos
n = int(input("¿Cuántos elementos desea ingresar en la lista? "))

# Crear la lista con los elementos ingresados
lista = []
for i in range(n):
    elemento = input(f"Ingrese el elemento {i + 1}: ")
    lista.append(elemento)

# Mostrar la lista normal e invertida
print("\nLista original:", lista)
print("Lista invertida:", list(reversed(lista)))