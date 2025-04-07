#ejercicio 1 =

print(" Calculadora Multiformato ")

try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    print(f"Suma: {num1} + {num2} = {num1 + num2}")
    print(f"Resta: {num1} - {num2} = {num1 - num2}")
    print(f"Producto: {num1} * {num2} = {num1 * num2}")

    try:
        print(f"División: {num1} / {num2} = {num1 / num2}")
        print(f"Residuo: {num1} % {num2} = {num1 % num2}")
    except ZeroDivisionError:
        print("Error: División por cero no permitida.")

    print(f"Potencia: {num1} ** {num2} = {num1 ** num2}")

except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")

#ejercicio 2 =

print(" Conversión entre Sistemas Numéricos ")

opcion = input("¿Desea convertir de decimal a otros formatos (1) o de otros formatos a decimal (2)? ")

if opcion == "1":
    try:
        num = int(input("Ingrese un número decimal: "))
        print(f"Decimal: {num}")
        print(f"Binario: {bin(num)[2:]}")
        print(f"Octal: {oct(num)[2:]}")
        print(f"Hexadecimal: {hex(num)[2:].upper()}")
    except ValueError:
        print("Por favor, ingrese un número decimal válido.")

elif opcion == "2":
    numero = input("Ingrese el número: ")
    try:
        base = int(input("Ingrese la base del número (2, 8, 16): "))
        decimal = int(numero, base)
        print(f"El número {numero} en base {base} es {decimal} en decimal.")
    except ValueError:
        print("Error: Formato no válido para la base especificada.")

else:
    print("Opción no válida. Intente de nuevo.")

#ejercicio 3 =

print(" Control de Precios y Descuentos ")

try:
    nombre_producto = input("Ingrese el nombre del producto: ")
    precio_original = float(input("Ingrese el precio original: $"))
    descuento = float(input("Ingrese el porcentaje de descuento: "))

    valor_descuento = precio_original * (descuento / 100)
    precio_final = precio_original - valor_descuento

    print("\n Resumen del Producto ")
    print(f"Producto: {nombre_producto}")
    print(f"Precio Original: ${precio_original:.2f}")
    print(f"Descuento ({descuento}%): -${valor_descuento:.2f}")
    print(f"Precio Final: ${precio_final:.2f}")

except ValueError:
    print("Por favor, ingrese valores numéricos válidos para el precio y el descuento.")

#ejercicio 4 =

print(" Análisis Detallado de una Frase ")

frase = input("Ingrese una frase: ")

print("\n Análisis de la Frase ")
print(f"Longitud total: {len(frase)} caracteres")
print(f"Letra inicial: '{frase[0]}'")
print(f"Letra final: '{frase[-1]}'")
print(f"Sección intermedia: '{frase[len(frase)//4:3*len(frase)//4]}'")
print(f"En mayúsculas: '{frase.upper()}'")
print(f"En minúsculas: '{frase.lower()}'")

caracter = input("Ingrese un carácter para contar su frecuencia: ")
conteo = frase.count(caracter)
print(f"El carácter '{caracter}' aparece {conteo} veces.")

#ejercicio 5 =

try:
    salario = float(input("Ingrese la remuneración actual: $"))
    tiempo = int(input("Ingrese el tiempo en la empresa (en años): "))
    porcentaje_bonificacion = 0.05  # 5% por cada año

    bonificacion = salario * (porcentaje_bonificacion * tiempo)
    nuevo_salario = salario + bonificacion

    print(f"\nBonificación calculada:")
    print(f"Salario actual: ${salario:,.2f}")
    print(f"Bonificación: ${bonificacion:,.2f}")
    print(f"Nuevo salario total: ${nuevo_salario:,.2f}")

except ValueError:
    print("Error: Por favor, ingrese valores numéricos válidos.")
