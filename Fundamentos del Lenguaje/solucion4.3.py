def control_acceso():
    """
    Controla el acceso a un evento exclusivo basado en la edad y la invitación.
    """

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

# Ejemplo de uso
control_acceso()