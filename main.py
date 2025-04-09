# main.py
tarea = input("Escribe una nueva tarea: ")
with open("tareas.txt", "a") as archivo:
    archivo.write(tarea + "\n")
print("Tarea guardada.")
