import matematicas  

# Solicitar al usuario que ingrese los valores
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

# Usar las funciones del archivo matematicas.py
print("Sumar:", matematicas.sumar(a, b))
print("Restar:", matematicas.restar(a, b))
print("Multiplicar:", matematicas.multiplicar(a, b))
print("Dividir:", matematicas.dividir(a, b))