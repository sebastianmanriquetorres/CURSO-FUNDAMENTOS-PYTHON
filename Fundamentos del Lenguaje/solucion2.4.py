#solucion 1
# Pedir al usuario un número
numero = int(input("Ingresa un número: "))

# Mostrar la tabla de multiplicar del número ingresado
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} × {i} = {numero * i}")

#solucion 2
def calcular_descuento(estrato, edad, precio_boleta):
    if estrato == 1:
        if edad < 18:
            descuento = 0.20
        else:
            descuento = 0.15
    elif estrato == 2:
        if edad < 18:
            descuento = 0.10
        else:
            descuento = 0.05
    else:
        descuento = 0

    # Cálculo del valor de la boleta después del descuento
    valor_con_descuento = precio_boleta * (1 - descuento)
    return valor_con_descuento, descuento


def calcular_recaudo(N, precio_boleta):
    total_recaudado = 0
    total_descuentos = 0

    for i in range(N):
        estrato = int(input(f"Ingrese el estrato de la persona {i+1}: "))
        edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
        
        valor_con_descuento, descuento = calcular_descuento(estrato, edad, precio_boleta)
        
        total_recaudado += valor_con_descuento
        total_descuentos += precio_boleta * descuento

    return total_recaudado, total_descuentos


# Ingresamos el precio de la boleta y el número de personas
precio_boleta = float(input("Ingrese el precio de la boleta: "))
N = int(input("Ingrese el número de personas: "))

# Calcular el total recaudado y el total de descuentos
total_recaudado, total_descuentos = calcular_recaudo(N, precio_boleta)

# Mostrar el resultado
print(f"\nTotal recaudado: {total_recaudado:.2f}")
print(f"Total de descuentos aplicados: {total_descuentos:.2f}")

#solucion 3
# Definimos el password correcto
password_correcto = "miContraseña123"
intentos_fallidos = 0
max_intentos = 5

while intentos_fallidos < max_intentos:
    # Pedimos al usuario que ingrese su password
    password_ingresado = input("Ingrese su password: ")
    
    # Comprobamos si el password ingresado es correcto
    if password_ingresado == password_correcto:
        print("¡Bienvenido al programa!")
        break # Si el password es correcto, salimos del bucle
    else:
        intentos_fallidos += 1
        print(f"Password incorrecto. Intento {intentos_fallidos} de {max_intentos}")
        
# Si se alcanzan los 5 intentos fallidos
if intentos_fallidos == max_intentos:
    print("Número máximo de intentos alcanzado. El programa se cerrará.")