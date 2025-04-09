def guardar_tarea():
    tarea = input("Escribe una nueva tarea: ")
    with open("tareas.txt", "a") as archivo:
        archivo.write(tarea + "\n")
    print("Tarea guardada.")

def ver_tareas():
    print("\nTus tareas:")
    try:
        with open("tareas.txt", "r") as archivo:
            tareas = archivo.read()
            if tareas.strip() == "":
                print("No tienes tareas pendientes.")
            else:
                print(tareas)
    except FileNotFoundError:
        print("Aún no existe el archivo de tareas.")

while True:
    print("\n--- MENÚ DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        guardar_tarea()
    elif opcion == "2":
        ver_tareas()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida.")
