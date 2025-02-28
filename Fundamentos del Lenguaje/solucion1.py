# Función para calcular el índice de cosecha
def calcular_indice_cosecha(frutos_recolectados, frutos_producidos):
    if frutos_producidos == 0:  # Para evitar división por cero
        return 0
    indice_cosecha = (frutos_recolectados / frutos_producidos) * 100
    return indice_cosecha

# Recibir datos del usuario
frutos_recolectados = float(input("Introduce la cantidad de frutos recolectados: "))
frutos_producidos = float(input("Introduce la cantidad total de frutos producidos: "))

# Calcular el índice de cosecha
indice = calcular_indice_cosecha(frutos_recolectados, frutos_producidos)

# Mostrar el resultado
print(f"El índice de cosecha es: {indice:.2f}%")