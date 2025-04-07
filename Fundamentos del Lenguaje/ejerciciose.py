#ejercicio 1 =

print(" Adivina el Número Secreto ")
print("Un amigo debe pensar en un número entre 1 y 100.")
numero_secreto = int(input("Amigo, ingresa el número secreto (no lo mires si eres quien va a adivinar): "))
print("\n¡Ahora intenta adivinar el número!")

intentos = 0

while True:
    try:
        intento = int(input("Ingresa tu número: "))
        intentos += 1

        if intento < numero_secreto:
            print(" El número secreto es mayor. ¡Sigue intentando!")
        elif intento > numero_secreto:
            print(" El número secreto es menor. ¡Sigue intentando!")
        else:
            print(f" ¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
            break
    except ValueError:
        print(" Por favor, ingresa un número válido.")

#ejercicio 2 =

while True:
    contrasena = input("Introduce una contraseña segura: ")

    tiene_mayus = False
    tiene_minus = False
    tiene_num = False

    if len(contrasena) >= 8:
        for caracter in contrasena:
            if caracter.islower():
                tiene_minus = True
            elif caracter.isupper():
                tiene_mayus = True
            elif caracter.isdigit():
                tiene_num = True

    if tiene_mayus and tiene_minus and tiene_num:
        break
    else:
        print("Contraseña insegura. Por favor, inténtalo de nuevo.")

print("Contraseña segura introducida.")

#ejercicio 3 =

try:
    edad = int(input("Ingrese su edad: "))
    invitacion = input("¿Tiene una invitación especial? (sí/no): ").lower()

    if edad >= 18 and invitacion == "sí":
        print("Acceso permitido. Bienvenido al evento exclusivo.")
    elif edad >= 21:
        print("Acceso permitido. Bienvenido al evento exclusivo.")
    else:
        print("Acceso denegado. Lo sentimos, no cumple con los requisitos para acceder al evento.")

except ValueError:
    print("Error: Ingrese una edad válida (número entero).")

#ejercicio 4 =

numero = int(input("Introduce un número entero: "))

if numero < 0:
    print("El factorial no está definido para números negativos.")
elif numero == 0:
    print("El factorial de 0 es: 1")
else:
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    print(f"El factorial de {numero} es: {factorial}")

#ejercicio 5 =

try:
    numero = int(input("Ingrese un número entero: "))
    limite = 10

    print(f"\nTabla de multiplicar del {numero}")
    for i in range(1, limite + 1):
        print(f"{numero} x {i} = {numero * i}")

except ValueError:
    print("Error: Por favor, ingrese un número entero válido.")


