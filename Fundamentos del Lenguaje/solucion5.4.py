def analizar_frase(frase):
    print(" Análisis de la Frase ")
    print(f"Longitud total: {len(frase)} caracteres")
    print(f"Letra inicial: '{frase[0]}'")
    print(f"Letra final: '{frase[-1]}'")
    print(f"Sección intermedia: '{frase[len(frase)//4:3*len(frase)//4]}'")
    print(f"En mayúsculas: '{frase.upper()}'")
    print(f"En minúsculas: '{frase.lower()}'")

    caracter = input("Ingrese un carácter para contar su frecuencia: ")
    conteo = frase.count(caracter)
    print(f"El carácter '{caracter}' aparece {conteo} veces.")


def main():
    print(" Análisis Detallado de una Frase ")
    frase = input("Ingrese una frase: ")
    analizar_frase(frase)


if __name__ == "__main__":
    main()
