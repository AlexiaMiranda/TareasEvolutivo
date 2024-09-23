from Tarea3Evolutivo import ejemplarTSP
from ejemplarTSP import *
from solucionTSP import *

file_path = str(input("Ingrese el nombre del archivo: "))
tsp = ejemplarTSP.leer_archivo(file_path)
solucion = []
while True:
    print("\nEscribe una opción: ")
    print("1 para generar solución aleatoria")
    print("2 para evaluar una solución aleatoria")
    print("3 para intercambiar dos elementos consecutivos")
    print("4 para intercambiar dos elementos no consecutivos")
    print("5 salir")
    opcion = input()

    if opcion == '1':
        sol_aleatoria(file_path)
        solucion = leer_archivo("out_file.txt")
        

    elif opcion == '2':
        evaluar_sol_aleatoria("out_file.txt")

    
    elif opcion == '3':
        solucion = cambiar_consecutivos("out_file.txt")
        evaluar_sol_aleatoria(solucion)
    
    elif opcion == '4':
        solucion = cambiar_noconsecutivos("out_file.txt")
        evaluar_sol_aleatoria(solucion)

    elif opcion == '5':
        break

    else:
        print("Opción no válida")