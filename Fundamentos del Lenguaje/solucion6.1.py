def administrar_actividades(actividades):
    print("Lista de actividades (estado inicial):")
    for i, actividad in enumerate(actividades, start=1):
        print(f"Posición {i}: {actividad}")

    # Filtrar actividades completadas
    actividades_filtradas = [act for act in actividades if not act.endswith("[✔]")]

    print("\nLista de actividades (después de filtrar las completadas):")
    for i, actividad in enumerate(actividades_filtradas, start=1):
        print(f"Posición {i}: {actividad}")


# Ejemplo de uso
actividades = [
    "Hacer ejercicio [✔]",
    "Preparar desayuno",
    "Revisar correos [✔]",
    "Estudiar programación",
    "Limpiar la casa [✔]"
]

administrar_actividades(actividades)