def informe_alumnos(nombres, calificaciones):
    print("Informe de Alumnos:")
    for i, (nombre, calificacion) in enumerate(zip(nombres, calificaciones), start=1):
        print(f"Posición {i}: {nombre} - Nota: {calificacion}")

    while True:
        try:
            posicion = int(input("\nIngrese la posición del alumno para consultar su nota (0 para salir): "))
            if posicion == 0:
                print("Consulta finalizada.")
                break
            if 1 <= posicion <= len(nombres):
                print(f"Nota de {nombres[posicion - 1]}: {calificaciones[posicion - 1]}")
            else:
                print("Posición fuera de rango.")
        except ValueError:
            print("Por favor, ingrese un número válido.")


# Ejemplo de uso
nombres = ["Ana", "Luis", "María", "Pedro", "Sofía"]
calificaciones = [85, 92, 78, 88, 95]
informe_alumnos(nombres, calificaciones)
