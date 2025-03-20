def calculadora(num1, num2):
    print(" Calculadora Multiformato ")
    print(f"Suma: {num1} + {num2} = {num1 + num2}")
    print(f"Resta: {num1} - {num2} = {num1 - num2}")
    print(f"Producto: {num1} * {num2} = {num1 * num2}")
    try:
        print(f"División: {num1} / {num2} = {num1 / num2}")
        print(f"Residuo: {num1} % {num2} = {num1 % num2}")
    except ZeroDivisionError:
        print(" Error: División por cero no permitida.")
    print(f"Potencia: {num1} ** {num2} = {num1 ** num2}")


def main():
    print(" Calculadora Multiformato ")
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        calculadora(num1, num2)
    except ValueError:
        print(" Por favor, ingrese valores numéricos válidos.")


if __name__ == "__main__":
    main()