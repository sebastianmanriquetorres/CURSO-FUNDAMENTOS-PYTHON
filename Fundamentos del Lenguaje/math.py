# Función de suma
def suma(a, b):
    return a + b

# Función de resta
def resta(a, b):
    return a - b

# Función de multiplicación
def multiplicacion(a, b):
    return a * b

# Función de división
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida"

# Ejemplo de uso de las funciones
num1 = 10
num2 = 5

print("Suma:", suma(num1, num2))
print("Resta:", resta(num1, num2))
print("Multiplicación:", multiplicacion(num1, num2))
print("División:", division(num1, num2))
