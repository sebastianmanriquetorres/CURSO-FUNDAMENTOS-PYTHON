def generar_tabla_de_multiplicar():
    try:
        # Pedir al usuario un número entero
        numero = int(input("Ingrese un número entero: "))

        # Establecer un límite preestablecido (por ejemplo, 10)
        limite = 10

        # Generar la tabla de multiplicar
        print(f"\n📊 Tabla de multiplicar del {numero} 📊")
        for i in range(1, limite + 1):
            producto = numero * i
            print(f"{numero} x {i} = {producto}")
    except ValueError:
        print("❌ Error: Por favor, ingrese un número entero válido.")

# Llamar a la función para generar la tabla de multiplicar
generar_tabla_de_multiplicar()