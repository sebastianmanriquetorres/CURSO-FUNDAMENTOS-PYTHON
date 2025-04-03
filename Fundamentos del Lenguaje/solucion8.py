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

#Ejercicios de apropiacion de Diccionario 2
