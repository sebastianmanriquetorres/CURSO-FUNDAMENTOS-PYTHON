print("Bienvenido a la inscripción para la universidad")
print("El valor de la matricula es de $25000000")
print("Se le solicitará unos datos para observar de cuanto será su descuento")
precio = 25000000
edad = int(input("ingrese su edad: "))
estrato = int(input("ingrese su estrato: "))
if estrato == 1 and edad < 18:
  print("el descuento que se le aplicará es del 20%")
  print("el valor a pagar es de: ", precio - (precio * 0.20))
elif estrato == 1 and edad >= 18:
  print("el descuento que se le aplicará es del 15%")
  print("el valor a pagar es de: ", precio - (precio * 0.15))
elif estrato == 2 and edad < 18:
  print("el descuento es del 10%")
  print("el valor a pagar es de: ", precio - (precio * 0.10))
elif estrato == 2 and edad >= 18:
  print("el descuento es del 5%")
  print("el valor a pagar es de: ", precio - (precio * 0.05))
elif edad >= 125:
  print("edad invalida")
else:
  print("no aplica descuento")
print("fin del programa")