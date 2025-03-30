import json

#cargar el inventario desde un archivo JSON si existe 

try:
    with open("inventario.json", "r") as file:
        inventario = json.load(file)
except FileNotFoundError:
  inventario = {
"producto A" : {"cantidad": 10, "umbral": 5},
"producto B" : {"cantidad": 3, "umbral": 4},
"producto C" : {"cantidad": 8, "umbral": 2},
}
  while True:
    print("\n--- Gestión de Inventario ---")
    print("1. Mostrar inventario")
    print("2. Actualizar stock")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        print("\nInventario actual:")
        for producto, datos in inventario.items():
            estado = "\u26A0 Bajo stock!" if datos["cantidad"] < datos["umbral"] else ""
            print(f"{producto}: {datos['cantidad']} unidades {estado}")
    
    elif opcion == "2":
        producto = input("Ingrese el nombre del producto a actualizar: ")
        if producto not in inventario:
            print("Producto no encontrado en el inventario.")
            continue
        
        try:
            cantidad_nueva = int(input("Ingrese la nueva cantidad: "))
            if cantidad_nueva < 0:
                print("La cantidad no puede ser negativa.")
                continue
            
            print("\nInventario antes de la actualización:")
            for p, d in inventario.items():
                estado = "\u26A0 Bajo stock!" if d["cantidad"] < d["umbral"] else ""
                print(f"{p}: {d['cantidad']} unidades {estado}")
            
            inventario[producto]["cantidad"] = cantidad_nueva
            with open("inventario.json", "w") as file:
                json.dump(inventario, file, indent=4)
            
            print("\nInventario después de la actualización:")
            for p, d in inventario.items():
                estado = "\u26A0 Bajo stock!" if d["cantidad"] < d["umbral"] else ""
                print(f"{p}: {d['cantidad']} unidades {estado}")
        
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
