#Ejercicios de apropiacion de conjuntos 1
frase = input("ingrese una frase: ")
caracteres_diferentes = set(frase)
print("caracteres diferenes en la frase:", caracteres_diferentes)

#Ejercicios de apropiacion de conjuntos 2
futbol = set()
baloncesto = set()

while True:
    print("\nMenú de Inscripción Deportiva")
    print("1. Inscribir estudiante")
    print("2. Mostrar estudiantes inscritos en fútbol")
    print("3. Mostrar estudiantes inscritos en baloncesto")
    print("4. Mostrar estudiantes inscritos en ambos deportes")
    print("5. Mostrar todos los estudiantes inscritos en algún deporte")
    print("6. Mostrar estudiantes inscritos en solo un deporte")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ")
        deporte = input("Ingrese el deporte (1 para fútbol, b para baloncesto, 1b para ambos): ")

        if "1" in deporte:
            futbol.add(nombre)
        if "b" in deporte:
            baloncesto.add(nombre)

    elif opcion == "2":
        print("\nEstudiantes inscritos en fútbol:", futbol)

    elif opcion == "3":
        print("\nEstudiantes inscritos en baloncesto:", baloncesto)

    elif opcion == "4":
        print("\nEstudiantes inscritos en ambos deportes:", futbol & baloncesto)

    elif opcion == "5":
        print("\nTodos los estudiantes inscritos en algún deporte:", futbol | baloncesto)

    elif opcion == "6":
        print("\nEstudiantes inscritos en solo un deporte:", (futbol ^ baloncesto))

    elif opcion == "7":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intente de nuevo.")

 #Ejercicios de apropiacion de Diccionario 1
frutas = {
    "manzana": "apple",
    "banana": "banana",
    "naranja": "orange",
    "pera": "pear",
    "uva": "grape",
    "fresa": "strawberry",
    "cereza": "cherry",
    "piña": "pineapple",
    "mango": "mango",
    "sandía": "watermelon"
}

fruta = input("Ingrese el nombre de una fruta en español: ").lower()

if fruta in frutas:
    print("La traducción al inglés es:", frutas[fruta])
else:
    print("Lo siento, la fruta no está en la lista.")
    agregar = input("¿Desea agregar esta fruta a la lista? (si/no): ").lower()
    
    if agregar == "si":
        traduccion = input(f"Ingrese la traducción al inglés de '{fruta}': ").lower()
        frutas[fruta] = traduccion
        print(f"\nFruta '{fruta}' agregada con la traducción '{traduccion}'.")
        print("\nLista actualizada de frutas:")
        for esp, ing in frutas.items():
            print(f"{esp} -> {ing}")
    else:
        print("No se ha agregado la fruta.")

#Ejercicios de apropiacion de Diccionario 2

# Listas de ejemplo (puedes modificarlas o permitir ingreso por el usuario)
futbol = {"Ana", "Luis", "Carlos", "Sofía"}
baloncesto = {"Luis", "María", "Pedro", "Sofía"}

opcion = ""

while opcion != "6":
    print("\n--- Menú de Deportes ---")
    print("1. Estudiantes inscritos en fútbol")
    print("2. Estudiantes inscritos en baloncesto")
    print("3. Estudiantes inscritos en ambos deportes")
    print("4. Todos los estudiantes inscritos en algún deporte")
    print("5. Estudiantes inscritos en solo un deporte")
    print("6. Salir")

    opcion = input("Seleccione una opción (1-6): ")

    if opcion == "1":
        print("\nEstudiantes en fútbol:")
        for estudiante in futbol:
            print("-", estudiante)

    elif opcion == "2":
        print("\nEstudiantes en baloncesto:")
        for estudiante in baloncesto:
            print("-", estudiante)

    elif opcion == "3":
        ambos = futbol.intersection(baloncesto)
        print("\nEstudiantes inscritos en ambos deportes:")
        if ambos:
            for estudiante in ambos:
                print("-", estudiante)
        else:
            print("Ningún estudiante está en ambos deportes.")

    elif opcion == "4":
        todos = futbol.union(baloncesto)
        print("\nTodos los estudiantes inscritos en algún deporte:")
        for estudiante in todos:
            print("-", estudiante)

    elif opcion == "5":
        solo_un_deporte = futbol.symmetric_difference(baloncesto)
        print("\nEstudiantes inscritos en solo un deporte:")
        for estudiante in solo_un_deporte:
            print("-", estudiante)

    elif opcion == "6":
        print("¡Hasta luego!")

    else:
        print("Opción inválida. Intenta nuevamente.")
