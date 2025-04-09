print("Bienvenido al gestor de tareas\n")
print("Tus tareas:")

try:
    with open("tareas.txt", "r") as archivo:
        tareas = archivo.read()
        if tareas.strip() == "":
            print("No tienes tareas pendientes.")
        else:
            print(tareas)
except FileNotFoundError:
    print("Aún no existe el archivo de tareas.")
