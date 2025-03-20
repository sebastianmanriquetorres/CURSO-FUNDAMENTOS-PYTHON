import random

def adivina_numero_secreto():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print(" Adivina el Número Secreto ")
    print("He pensado en un número entre 1 y 100. ¡Intenta adivinarlo!")

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


if __name__ == "__main__":
    adivina_numero_secreto()
