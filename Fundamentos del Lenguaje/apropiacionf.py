#ejercicio 1 =

def separar_pares_impares(numeros):
    """
    Toma una lista de números enteros y devuelve dos listas ordenadas:
    una con los números pares y otra con los impares.
    """
    pares = []
    impares = []

    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    return sorted(pares), sorted(impares)

if __name__ == "__main__":
    lista = [5, 2, 8, 3, 1, 4, 7, 6]
    pares, impares = separar_pares_impares(lista)

    print("Lista original:", lista)
    print("Números pares ordenados:", pares)
    print("Números impares ordenados:", impares)

#ejercicio 2 =

def contar_letras(palabra):
    """
    Recibe una palabra y devuelve un diccionario donde las claves son 
    las letras únicas y los valores son la cantidad de veces que aparece cada una.
    """
    contador = {}

    for letra in palabra:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1

    return contador

if __name__ == "__main__":
    palabra = input("Ingresa una palabra: ")
    resultado = contar_letras(palabra)

    print("\nConteo de letras:")
    for letra, cantidad in resultado.items():
        print(f"'{letra}': {cantidad}")

#ejercicio 3 =

def numero_a_palabras(numero):
    """
    Recibe un número entero y devuelve una cadena con los nombres 
    de sus dígitos separados por guiones.
    """
    nombres_digitos = {
        '0': 'cero',
        '1': 'uno',
        '2': 'dos',
        '3': 'tres',
        '4': 'cuatro',
        '5': 'cinco',
        '6': 'seis',
        '7': 'siete',
        '8': 'ocho',
        '9': 'nueve'
    }

    numero_str = str(abs(numero))  # Convertir a string y manejar negativos
    palabras = [nombres_digitos[d] for d in numero_str]
    resultado = '-'.join(palabras)

    # Agregar "menos" si el número era negativo
    if numero < 0:
        resultado = "menos-" + resultado

    return resultado

if __name__ == "__main__":
    numero = int(input("Ingresa un número: "))
    resultado = numero_a_palabras(numero)
    print("Resultado:", resultado)
