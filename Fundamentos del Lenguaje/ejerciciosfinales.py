#ejercicio 1 = Calculadora Avanzada

def calculadora():
    try:
        # Solicitar al usuario los números y el operador
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        operador = input("Ingrese el operador (+, -, *, /, **, //): ")

        # Realizar la operación según el operador
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            if num2 == 0:
                raise ZeroDivisionError("No se puede dividir entre cero.")
            resultado = num1 / num2
        elif operador == '**':
            resultado = num1 ** num2
        elif operador == '//':
            if num2 == 0:
                raise ZeroDivisionError("No se puede dividir entre cero.")
            resultado = num1 // num2
        else:
            raise ValueError("Operador no válido.")

        print(f"Resultado: {num1} {operador} {num2} = {resultado}")

    except ValueError as ve:
        print(f"Error de valor: {ve}")
    except ZeroDivisionError as zde:
        print(f"Error matemático: {zde}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Ejecutar la calculadora
calculadora()

#ejercicio 2 = Administrador de Inventarios

def mostrar_inventario(inventario):
    print("Inventario actual:")
    for producto, cantidad in inventario.items():
        print(f"- {producto}: {cantidad} unidades")
    print()

def agregar_producto(inventario, producto, cantidad):
    if producto in inventario:
        print(f"El producto '{producto}' ya existe. Usa la función de actualización.")
    else:
        inventario[producto] = cantidad
        print(f"Producto '{producto}' agregado con {cantidad} unidades.")

def actualizar_producto(inventario, producto, cantidad):
    try:
        if producto not in inventario:
            raise KeyError
        inventario[producto] = cantidad
        print(f"Stock de '{producto}' actualizado a {cantidad} unidades.")
    except KeyError:
        print(f"Error: El producto '{producto}' no existe en el inventario.")

def eliminar_producto(inventario, producto):
    try:
        if producto not in inventario:
            raise KeyError
        del inventario[producto]
        print(f"Producto '{producto}' eliminado del inventario.")
    except KeyError:
        print(f"Error: El producto '{producto}' no existe en el inventario.")

# Inventario inicial
inventario = {'manzanas': 50, 'naranjas': 30, 'peras': 20}
print("Inventario inicial:")
mostrar_inventario(inventario)

# Operaciones de ejemplo
print("Actualizando stock de 'peras' a 25...")
actualizar_producto(inventario, 'peras', 25)

print("Agregando 'bananas' con 40 unidades...")
agregar_producto(inventario, 'bananas', 40)

print("Eliminando 'naranjas'...")
eliminar_producto(inventario, 'naranjas')

# Inventario final
print("Inventario final:")
mostrar_inventario(inventario)

#ejercicio 3 = Análisis de Texto

import re

def analizar_texto(texto):
    try:
        if not texto.strip():
            raise ValueError("El texto no puede estar vacío.")

        # Convertir a minúsculas y extraer palabras usando expresión regular
        palabras = re.findall(r'\b\w+\b', texto.lower())

        frecuencia = {}
        for palabra in palabras:
            if palabra in frecuencia:
                frecuencia[palabra] += 1
            else:
                frecuencia[palabra] = 1

        print("Frecuencia de palabras:")
        for palabra, cantidad in frecuencia.items():
            print(f"{palabra}: {cantidad}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Solicitar texto al usuario
entrada = input("Ingrese un texto: ")
analizar_texto(entrada)

#ejercicio 4 = Conversor de Unidades

def cm_a_pulgadas(cm):
    return cm / 2.54

def km_a_millas(km):
    return km * 0.621371

def conversor_unidades():
    try:
        print("Seleccione la conversión:\n")
        print("1. Centímetros a pulgadas")
        print("2. Kilómetros a millas")
        opcion = input("Opción (1 o 2): ")

        if opcion not in ['1', '2']:
            raise ValueError("Opción no válida. Debe ser 1 o 2.")

        cantidad = input("Ingrese la cantidad a convertir: ")

        # Intentar convertir a número
        cantidad = float(cantidad)

        if opcion == '1':
            resultado = cm_a_pulgadas(cantidad)
            print(f"Resultado: {cantidad} cm = {round(resultado, 2)} pulgadas")
        elif opcion == '2':
            resultado = km_a_millas(cantidad)
            print(f"Resultado: {cantidad} km = {round(resultado, 2)} millas")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Ejecutar el conversor
conversor_unidades()

#ejercicio 5 = Juego "Adivina el Número"

import random

def adivina_el_numero():
    print('¡Bienvenido al juego "Adivina el Número"!')
    print("Estoy pensando en un número entre 1 y 50.")
    
    numero_secreto = random.randint(1, 50)
    intento = 1

    while True:
        try:
            adivinanza = int(input(f"Intento {intento} - Ingresa tu número: "))
            
            if adivinanza < 1 or adivinanza > 50:
                print("Por favor, ingresa un número dentro del rango de 1 a 50.")
                continue

            if adivinanza < numero_secreto:
                print("El número secreto es mayor.")
            elif adivinanza > numero_secreto:
                print("El número secreto es menor.")
            else:
                print(f"¡Felicidades! Has adivinado el número secreto: {numero_secreto}")
                break  # Salir del bucle al adivinar
            intento += 1

        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

# Ejecutar el juego
adivina_el_numero()

#ejercicio 6 = Calculadora de Factorial

def calcular_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main():
    try:
        numero = int(input("Ingrese un número entero para calcular su factorial: "))
        if numero < 0:
            raise ValueError("El número no puede ser negativo.")
        
        resultado = calcular_factorial(numero)
        print(f"El factorial de {numero} es {resultado}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Ejecutar la función principal
main()

#ejercicio 7 = Manejo de Fechas y Horas

from datetime import datetime

def dias_para_fecha():
    try:
        entrada = input("Ingrese una fecha (DD/MM/AAAA): ")
        
        # Intentar convertir la entrada a un objeto datetime
        fecha_objetivo = datetime.strptime(entrada, "%d/%m/%Y").date()
        fecha_actual = datetime.now().date()
        
        # Calcular la diferencia de días
        diferencia = (fecha_objetivo - fecha_actual).days

        if diferencia > 0:
            print(f"Faltan {diferencia} días para el {entrada}.")
        elif diferencia == 0:
            print(f"¡Hoy es el día {entrada}!")
        else:
            print(f"La fecha {entrada} ya pasó hace {-diferencia} días.")

    except ValueError:
        print("Formato de fecha inválido. Asegúrate de usar el formato DD/MM/AAAA.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Ejecutar la función
dias_para_fecha()

#ejercicio 8 = Registro de Estudiantes

def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar estudiante")
    print("2. Actualizar calificación")
    print("3. Eliminar estudiante")
    print("4. Listar estudiantes")
    print("5. Salir")

def agregar_estudiante(registro):
    try:
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre in registro:
            print(f"El estudiante '{nombre}' ya está registrado.")
            return
        calificacion = float(input("Ingrese la calificación: "))
        registro[nombre] = calificacion
        print(f"Estudiante agregado: {nombre} - {calificacion}")
    except ValueError:
        print("Error: La calificación debe ser un número.")

def actualizar_calificacion(registro):
    try:
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre not in registro:
            raise KeyError(f"El estudiante '{nombre}' no existe.")
        calificacion = float(input("Ingrese la nueva calificación: "))
        registro[nombre] = calificacion
        print(f"Estudiante actualizado: {nombre} - {calificacion}")
    except KeyError as e:
        print(e)
    except ValueError:
        print("Error: La calificación debe ser un número.")

def eliminar_estudiante(registro):
    try:
        nombre = input("Ingrese el nombre del estudiante a eliminar: ")
        if nombre not in registro:
            raise KeyError(f"El estudiante '{nombre}' no existe.")
        del registro[nombre]
        print(f"Estudiante '{nombre}' eliminado.")
    except KeyError as e:
        print(e)

def listar_estudiantes(registro):
    print("\nRegistro de estudiantes:")
    if not registro:
        print("No hay estudiantes registrados.")
    else:
        for nombre, calificacion in registro.items():
            print(f"- {nombre}: {calificacion}")

def main():
    registro = {'Ana': 90, 'Luis': 78, 'Carlos': 85}
    print("Registro de estudiantes inicial:")
    listar_estudiantes(registro)

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Opción: "))
            if opcion == 1:
                agregar_estudiante(registro)
            elif opcion == 2:
                actualizar_calificacion(registro)
            elif opcion == 3:
                eliminar_estudiante(registro)
            elif opcion == 4:
                listar_estudiantes(registro)
            elif opcion == 5:
                print("\nRegistro final:")
                listar_estudiantes(registro)
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente de nuevo.")
        except ValueError:
            print("Error: Ingrese un número del 1 al 5.")

# Ejecutar el programa
main()

#ejercicio 9 = Generador de Contraseñas Aleatorias

import random

def generar_contrasena(longitud):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/`~"
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def main():
    try:
        longitud = int(input("Ingrese la longitud deseada para la contraseña: "))
        if longitud <= 0:
            raise ValueError("La longitud debe ser un número entero positivo.")
        
        contrasena = generar_contrasena(longitud)
        print(f"Contraseña generada: {contrasena}")
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Ejecutar el generador
main()

#ejercicio 10 = Buscador de Archivos en un Directorio

import os

def buscar_archivos(directorio, subcadena):
    try:
        # Verificar si el directorio existe
        if not os.path.isdir(directorio):
            raise FileNotFoundError(f"El directorio '{directorio}' no existe.")
        
        # Listar archivos en el directorio
        archivos = os.listdir(directorio)
        
        # Filtrar archivos que contienen la subcadena
        archivos_encontrados = [archivo for archivo in archivos if subcadena.lower() in archivo.lower()]
        
        if archivos_encontrados:
            print(f"\nArchivos encontrados que contienen '{subcadena}':")
            for archivo in archivos_encontrados:
                print(archivo)
        else:
            print(f"No se encontraron archivos que contengan '{subcadena}'.")
    
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except PermissionError:
        print("Error: Permisos insuficientes para acceder a ese directorio.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def main():
    try:
        directorio = input("Ingrese la ruta del directorio: ")
        subcadena = input("Ingrese la subcadena a buscar: ")
        
        buscar_archivos(directorio, subcadena)
    
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el programa: {e}")

# Ejecutar el buscador
main()
