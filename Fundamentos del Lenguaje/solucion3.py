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