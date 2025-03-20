def calcular_descuento(precio, descuento):
    valor_descuento = precio * (descuento / 100)
    precio_final = precio - valor_descuento
    return valor_descuento, precio_final


def main():
    print(" Control de Precios y Descuentos ")
    try:
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio_original = float(input("Ingrese el precio original: $"))
        descuento = float(input("Ingrese el porcentaje de descuento: "))

        valor_descuento, precio_final = calcular_descuento(precio_original, descuento)

        print("\n Resumen del Producto ")
        print(f"Producto: {nombre_producto}")
        print(f"Precio Original: ${precio_original:.2f}")
        print(f"Descuento ({descuento}%): -${valor_descuento:.2f}")
        print(f"Precio Final: ${precio_final:.2f}")
    except ValueError:
        print(" Por favor, ingrese valores numéricos válidos para el precio y el descuento.")


if __name__ == "__main__":
    main()