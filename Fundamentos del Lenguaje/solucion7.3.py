estudiantes = {}

while True:
    print("\n--- Gestión de Estudiantes ---")
    print("1. Agregar estudiante y calificación")
    print("2. Listar estudiantes")
    print("3. Consultar calificación")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        nombre = input("Nombre del estudiante: ")
        calificacion = input("Calificación: ")
        estudiantes[nombre] = calificacion
        print("Registro agregado con éxito.")
    
    elif opcion == "2":
        print("\nLista de estudiantes:")
        for nombre, calificacion in estudiantes.items():
            print(f"{nombre}: {calificacion}")
    
    elif opcion == "3":
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre in estudiantes:
            print(f"Calificación de {nombre}: {estudiantes[nombre]}")
        else:
            print("Estudiante no encontrado.")
    
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")