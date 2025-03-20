import re

def validar_contrasena(contrasena):
    """
    Valida si una contraseña cumple con los criterios de seguridad.

    Args:
        contrasena (str): La contraseña a validar.

    Returns:
        bool: True si la contraseña es segura, False en caso contrario.
    """

    if len(contrasena) < 8:
        return False  # Longitud mínima de 8 caracteres

    if not re.search("[a-z]", contrasena):
        return False  # Debe contener al menos una letra minúscula

    if not re.search("[A-Z]", contrasena):
        return False  # Debe contener al menos una letra mayúscula

    if not re.search("[0-9]", contrasena):
        return False  # Debe contener al menos un número

    return True

def obtener_contrasena_segura():
    """
    Solicita al usuario una contraseña y la valida hasta que sea segura.

    Returns:
        str: La contraseña segura introducida por el usuario.
    """

    while True:
        contrasena = input("Introduce una contraseña segura: ")
        if validar_contrasena(contrasena):
            return contrasena
        else:
            print("Contraseña insegura. Por favor, inténtalo de nuevo.")

# Ejemplo de uso
contrasena_segura = obtener_contrasena_segura()
print("Contraseña segura introducida.")