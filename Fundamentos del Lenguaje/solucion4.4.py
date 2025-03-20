def calcular_factorial(numero):
    """
    Calcula el factorial de un número entero.

    Args:
        numero (int): El número del cual se calculará el factorial.

    Returns:
        int: El factorial del número dado.
    """

    if numero < 0:
        return "El factorial no está definido para números negativos."
    elif numero == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        return factorial

# Ejemplo de uso
numero = int(input("Introduce un número entero: "))
resultado = calcular_factorial(numero)
print(f"El factorial de {numero} es: {resultado}")