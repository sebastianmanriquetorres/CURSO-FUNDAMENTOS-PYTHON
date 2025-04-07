#Ejercicio 1 =

temperatura = int(input("ingrse la temperatura del motor"))
if temperatura >=80:
    print("el motor exede la temperatura, por ende será apagado")
else:
    print("el motor no exede la temperatura, por ende seguirá encendido")
print("fin del programa")

#Ejercicio 2 =

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

#Ejercicio 3 =

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

#Ejercicio 4 =

#solucion 1
numero = int(input("Ingresa un número: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} × {i} = {numero * i}")

#solucion 2 
precio_boleta = float(input("Ingrese el precio de la boleta: "))
N = int(input("Ingrese el número de personas: "))

total_recaudado = 0
total_descuentos = 0

for i in range(N):
    estrato = int(input(f"Ingrese el estrato de la persona {i+1}: "))
    edad = int(input(f"Ingrese la edad de la persona {i+1}: "))

    if estrato == 1:
        if edad < 18:
            descuento = 0.20
        else:
            descuento = 0.15
    elif estrato == 2:
        if edad < 18:
            descuento = 0.10
        else:
            descuento = 0.05
    else:
        descuento = 0

    valor_con_descuento = precio_boleta * (1 - descuento)
    total_recaudado += valor_con_descuento
    total_descuentos += precio_boleta * descuento

print(f"\nTotal recaudado: {total_recaudado:.2f}")
print(f"Total de descuentos aplicados: {total_descuentos:.2f}")

#solucion 3
password_correcto = "miContraseña123"
intentos_fallidos = 0
max_intentos = 5

while intentos_fallidos < max_intentos:
    password_ingresado = input("Ingrese su password: ")
    
    if password_ingresado == password_correcto:
        print("¡Bienvenido al programa!")
        break
    else:
        intentos_fallidos += 1
        print(f"Password incorrecto. Intento {intentos_fallidos} de {max_intentos}")

if intentos_fallidos == max_intentos:
    print("Número máximo de intentos alcanzado. El programa se cerrará.")