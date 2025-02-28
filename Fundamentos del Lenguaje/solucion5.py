# Recibir una frase del usuario
frase = input("Introduce una frase: ")

# Transformar la frase a mayúsculas y luego invertirla
frase_transformada = frase.upper()[::-1]

# Mostrar el resultado
print(f"La frase transformada es: {frase_transformada}")