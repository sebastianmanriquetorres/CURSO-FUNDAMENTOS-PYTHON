def procesar_numeros():
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


procesar_numeros()