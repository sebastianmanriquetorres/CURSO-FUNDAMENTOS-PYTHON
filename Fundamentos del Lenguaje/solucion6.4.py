def mostrar_menu():
    print("\nMenú de Operaciones:")
    print("1. Calcular la suma total de los valores")
    print("2. Reordenar valores de menor a mayor")
    print("3. Reordenar valores de mayor a menor")
    print("4. Eliminar un valor por posición")
    print("0. Salir")


def suma_total(valores):
    return sum(valores)


def reordenar(valores, ascendente=True):
    return sorted(valores, reverse=not ascendente)


def eliminar_valor(valores):
    try:
        posicion = int(input("Ingrese la posición del valor a eliminar: "))
        if 1 <= posicion <= len(valores):
            eliminado = valores.pop(posicion - 1)
            print(f"Valor {eliminado} eliminado correctamente.")
        else:
            print("Posición fuera de rango.")
    except ValueError:
        print("Por favor, ingrese un número válido.")


def main():
    valores = [10, 5, 20, 15, 30]
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 0:
                print("Aplicación finalizada.")
                break
            elif opcion == 1:
                print("Suma total de los valores:", suma_total(valores))
            elif opcion == 2:
                valores = reordenar(valores, ascendente=True)
                print("Valores ordenados de menor a mayor:", valores)
            elif opcion == 3:
                valores = reordenar(valores, ascendente=False)
                print("Valores ordenados de mayor a menor:", valores)
            elif opcion == 4:
                eliminar_valor(valores)
                print("Valores actuales:", valores)
            else:
                print("Opción no válida.")
        except ValueError:
            print("Por favor, ingrese un número válido.")


main()