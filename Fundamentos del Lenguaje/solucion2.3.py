numdepiezas = int(input("ingrese el número de piezas: "))
for p in range (numdepiezas):

  pieza = input("ingrese los estándares de calidad: ")
  if len (pieza ) == pieza.count("0") + pieza.count("1"):
    defectuosos = pieza.count("0")
    print(defectuosos)

    if defectuosos > 0:
      print ("La pieza debe ser rechazada")
    else:
      print ("Pieza aceptada")
      break
  else:
    print ("error en la pieza")