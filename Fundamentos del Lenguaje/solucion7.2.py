import re
frase =("ingrese una frase: ")
palabras = frase.split()
palabras_limpias = tuple(sorted(re.sub(r'[^a-zA-Z]', '', palabra) for palabra in palabras))

print("palabras procesadas y ordenadas:", palabras_limpias)