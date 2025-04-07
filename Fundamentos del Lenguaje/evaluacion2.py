#ejercicio 1 =

# Inventario base (predefinido)
inventario = {
    "producto A": {"cantidad": 10, "umbral": 5},
    "producto B": {"cantidad": 3, "umbral": 4},
    "producto C": {"cantidad": 8, "umbral": 2},
}

while True:
    print("\n--- Gestión de Inventario ---")
    print("1. Mostrar inventario")
    print("2. Actualizar stock")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\nInventario actual:")
        for producto in inventario:
            cantidad = inventario[producto]["cantidad"]
            umbral = inventario[producto]["umbral"]
            estado = " Bajo stock!" if cantidad < umbral else ""
            print(f"{producto}: {cantidad} unidades {estado}")

    elif opcion == "2":
        producto = input("Ingrese el nombre del producto a actualizar: ")
        if producto not in inventario:
            print("Producto no encontrado en el inventario.")
            continue

        try:
            cantidad_nueva = int(input("Ingrese la nueva cantidad: "))
            if cantidad_nueva < 0:
                print("La cantidad no puede ser negativa.")
                continue

            print("\nInventario antes de la actualización:")
            for p in inventario:
                cant = inventario[p]["cantidad"]
                umb = inventario[p]["umbral"]
                estado = " Bajo stock!" if cant < umb else ""
                print(f"{p}: {cant} unidades {estado}")

            inventario[producto]["cantidad"] = cantidad_nueva

            print("\nInventario después de la actualización:")
            for p in inventario:
                cant = inventario[p]["cantidad"]
                umb = inventario[p]["umbral"]
                estado = " Bajo stock!" if cant < umb else ""
                print(f"{p}: {cant} unidades {estado}")

        except ValueError:
            print("Por favor, ingrese un número válido.")

    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")

#ejercicio 2 =

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

#ejercicio 3 =

frase = input("Ingrese una frase: ")
palabras = frase.split()

# Limpiar caracteres que no son letras
palabras_limpias = []
for palabra in palabras:
    solo_letras = ""
    for caracter in palabra:
        if (caracter >= "a" and caracter <= "z") or (caracter >= "A" and caracter <= "Z"):
            solo_letras += caracter
    palabras_limpias.append(solo_letras)

# Ordenar alfabéticamente y convertir en tupla
palabras_ordenadas = tuple(sorted(palabras_limpias))

print("Palabras procesadas y ordenadas:", palabras_ordenadas)

#ejercicio 4 =

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

#ejercicio 5 =

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
