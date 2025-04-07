#Ejercicio 1 =

# Recibir datos del usuario
frutos_recolectados = float(input("Introduce la cantidad de frutos recolectados: "))
frutos_producidos = float(input("Introduce la cantidad total de frutos producidos: "))

# Calcular el índice de cosecha
if frutos_producidos == 0:
    indice = 0
else:
    indice = (frutos_recolectados / frutos_producidos) * 100

# Mostrar el resultado
print(f"El índice de cosecha es: {indice:.2f}%")

#Ejercicio 2 =

print("\n".join(["**", "    ", "    ", "*", "", "", ""]))

#Ejercicio 3 =

# Solicitar las tres calificaciones parciales
calificacion1 = float(input("Ingrese la primera calificación parcial: "))
calificacion2 = float(input("Ingrese la segunda calificación parcial: "))
calificacion3 = float(input("Ingrese la tercera calificación parcial: "))

# Solicitar la calificación del examen final
examen_final = float(input("Ingrese la calificación del examen final: "))

# Solicitar la calificación del trabajo final
trabajo_final = float(input("Ingrese la calificación del trabajo final: "))

# Calcular el promedio de las tres calificaciones parciales
promedio_parciales = (calificacion1 + calificacion2 + calificacion3) / 3

# Calcular la calificación final usando los porcentajes proporcionados
calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)

# Mostrar la calificación final
print(f"La calificación final del alumno es: {calificacion_final:.2f}")

#Ejercicio 4 =

# Recibir una frase del usuario
frase = input("Introduce una frase: ")

# Contar las palabras en la frase
numero_palabras = len(frase.split())

# Mostrar el número de palabras
print(f"El número de palabras en la frase es: {numero_palabras}")

#Ejercicio 5 =

# Recibir una frase del usuario
frase = input("Introduce una frase: ")

# Transformar la frase a mayúsculas y luego invertirla
frase_transformada = frase.upper()[::-1]

# Mostrar el resultado
print(f"La frase transformada es: {frase_transformada}")