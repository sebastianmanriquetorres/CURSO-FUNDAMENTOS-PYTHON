numeros = [10, 25, 37, 49, 58, 62]

while True:
    print("\n--- Gestión de Números ---")
    print("1. Calcular promedio")
    print("2. Encontrar máximo y mínimo")
    print("3. Eliminar un número")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        if numeros:
            promedio = sum(numeros) / len(numeros)
            print(f"Promedio: {promedio:.2f}")
        else:
            print("La colección está vacía.")
    
    elif opcion == "2":
        if numeros:
            print(f"Máximo: {max(numeros)}, Mínimo: {min(numeros)}")
        else:
            print("La colección está vacía.")
    
    elif opcion == "3":
        print("Números actuales:", numeros)
        try:
            num = int(input("Ingrese el número a eliminar: "))
            if num in numeros:
                numeros.remove(num)
                print("Número eliminado.")
            else:
                print("El número no está en la colección.")
        except ValueError:
            print("Entrada no válida. Ingrese un número entero.")
    
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
    
    print("Colección actualizada:", numeros)