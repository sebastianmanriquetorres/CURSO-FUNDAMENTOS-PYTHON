#ejercicio 1 =

numeros = list(range(1, 21))
divisibles = []
no_divisibles = 0
suma_divisibles = 0

print("Números divisibles por 2 y su posición:")
for i, num in enumerate(numeros, start=1):
    if num % 2 == 0:
        divisibles.append(num)
        suma_divisibles += num
        print(f"Posición {i}: {num}")
    else:
        no_divisibles += 1

print("\nCantidad de números no divisibles por 2:", no_divisibles)
print("Suma de números divisibles por 2:", suma_divisibles)

#ejercicio 2 =

actividades = [
    "Hacer ejercicio [✔]",
    "Preparar desayuno",
    "Revisar correos [✔]",
    "Estudiar programación",
    "Limpiar la casa [✔]"
]

print("Lista de actividades (estado inicial):")
for i, actividad in enumerate(actividades, start=1):
    print(f"Posición {i}: {actividad}")

actividades_filtradas = [act for act in actividades if not act.endswith("[✔]")]

print("\nLista de actividades (después de filtrar las completadas):")
for i, actividad in enumerate(actividades_filtradas, start=1):
    print(f"Posición {i}: {actividad}")

#ejercicio 3 =

entrada = input("Ingresa una secuencia de caracteres: ")

letras = [car for car in entrada if car.isalpha()]
resultado = tuple(letras)

print("Texto filtrado (solo letras):", resultado)

#ejercicio 4 =

nombres = ["Ana", "Luis", "María", "Pedro", "Sofía"]
calificaciones = [85, 92, 78, 88, 95]

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

#ejercicio 5 =

valores = [10, 5, 20, 15, 30]

while True:
    print("\nMenú de Operaciones:")
    print("1. Calcular la suma total de los valores")
    print("2. Reordenar valores de menor a mayor")
    print("3. Reordenar valores de mayor a menor")
    print("4. Eliminar un valor por posición")
    print("0. Salir")
    
    try:
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 0:
            print("Aplicación finalizada.")
            break
        elif opcion == 1:
            print("Suma total de los valores:", sum(valores))
        elif opcion == 2:
            valores = sorted(valores)
            print("Valores ordenados de menor a mayor:", valores)
        elif opcion == 3:
            valores = sorted(valores, reverse=True)
            print("Valores ordenados de mayor a menor:", valores)
        elif opcion == 4:
            try:
                posicion = int(input("Ingrese la posición del valor a eliminar: "))
                if 1 <= posicion <= len(valores):
                    eliminado = valores.pop(posicion - 1)
                    print(f"Valor {eliminado} eliminado correctamente.")
                else:
                    print("Posición fuera de rango.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
            print("Valores actuales:", valores)
        else:
            print("Opción no válida.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
