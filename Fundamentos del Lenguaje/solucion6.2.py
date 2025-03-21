def filtrar_letras(texto):
    letras = [car for car in texto if car.isalpha()]
    resultado = tuple(letras)  # Convertir en una estructura inmutable
    print("Texto filtrado (solo letras):", resultado)


# Solicitar la secuencia de caracteres al usuario
entrada = input("Ingresa una secuencia de caracteres: ")
filtrar_letras(entrada)