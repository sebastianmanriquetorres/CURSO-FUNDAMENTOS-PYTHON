texto = input("Ingrese un párrafo: ").lower()
palabra = input("Ingrese la palabra a buscar: ").lower()

contador = texto.count(palabra)
posiciones = []
indice = texto.find(palabra)

while indice != -1:
    posiciones.append(indice)
    indice = texto.find(palabra, indice + 1)

print(f"La palabra '{palabra}' aparece {contador} veces.")
print("Posiciones:", posiciones if posiciones else "No encontrada")
