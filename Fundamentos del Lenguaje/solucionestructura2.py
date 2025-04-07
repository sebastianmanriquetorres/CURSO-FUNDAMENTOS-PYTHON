#Ejercicio 1 =

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

#Ejercicio 2 =

# Crear una lista de números
numeros = [1, 2, 3, 4, 5, 2, 6, 2, 7]

# Solicitar un número al usuario
numero_a_eliminar = int(input("Introduce el número que deseas eliminar: "))

# Eliminar todas las ocurrencias del número en la lista
while numero_a_eliminar in numeros:
    numeros.remove(numero_a_eliminar)

# Presentar la lista final
print("Lista final después de eliminar el número:", numeros)

#Ejercicio 3 =

frase1 = input("Ingresa la primera frase: ")
frase2 = input("Ingresa la segunda frase: ")

letras_iguales = []
min_longitud = min(len(frase1), len(frase2))

for i in range(min_longitud):
    if frase1[i] == frase2[i]:
        letras_iguales.append(frase1[i])

print(f"Letras repetidas en la misma posición: {letras_iguales}")

