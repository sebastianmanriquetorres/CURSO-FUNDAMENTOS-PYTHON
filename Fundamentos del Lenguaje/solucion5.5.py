def calcular_bonificacion():
    try:
        # Pedir al usuario los datos del trabajador
        salario = float(input("Ingrese la remuneración actual: $"))
        tiempo = int(input("Ingrese el tiempo en la empresa (en años): "))
        porcentaje_bonificacion = 0.05  # 5% de bonificación por cada año

        # Calcular la bonificación y el nuevo salario
        bonificacion = salario * (porcentaje_bonificacion * tiempo)
        nuevo_salario = salario + bonificacion

        # Mostrar los resultados
        print(f"\nBonificación calculada:")
        print(f"Salario actual: ${salario:,.2f}")
        print(f"Bonificación: ${bonificacion:,.2f}")
        print(f"Nuevo salario total: ${nuevo_salario:,.2f}")
    except ValueError:
        print("Error: Por favor, ingrese valores numéricos válidos.")

# Llamar a la función para calcular la bonificación
calcular_bonificacion()