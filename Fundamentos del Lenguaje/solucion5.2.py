def decimal_a_otros(num):
    print(f"Decimal: {num}")
    print(f"Binario: {bin(num)[2:]}")
    print(f"Octal: {oct(num)[2:]}")
    print(f"Hexadecimal: {hex(num)[2:].upper()}")


def otros_a_decimal(num, base):
    try:
        decimal = int(num, base)
        print(f"El número {num} en base {base} es {decimal} en decimal.")
    except ValueError:
        print(" Error: Formato no válido para la base especificada.")


def main():
    print(" Conversión entre Sistemas Numéricos ")
    opcion = input("¿Desea convertir de decimal a otros formatos (1) o de otros formatos a decimal (2)? ")
    if opcion == "1":
        try:
            numero = int(input("Ingrese un número decimal: "))
            decimal_a_otros(numero)
        except ValueError:
            print(" Por favor, ingrese un número decimal válido.")
    elif opcion == "2":
        numero = input("Ingrese el número: ")
        base = int(input("Ingrese la base del número (2, 8, 16): "))
        otros_a_decimal(numero, base)
    else:
        print(" Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()