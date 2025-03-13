def letras_repetidas(frase1, frase2):

  letras_iguales = []
  min_longitud = min(len(frase1), len(frase2))
  for i in range(min_longitud):
    if frase1[i] == frase2[i]:
      letras_iguales.append(frase1[i])
  return letras_iguales


frase1 = input("Ingresa la primera frase: ")
frase2 = input("Ingresa la segunda frase: ")

resultado = letras_repetidas(frase1, frase2)
print(f"Letras repetidas en la misma posición: {resultado}")