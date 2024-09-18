import random
import math
from ejemplarTSP import TSP
from ejemplarTSP import leer_archivo
"""Generar una solucion/permutación aleatoria"""
def sol_aleatoria(file_path ):
    ejemplar_tsp = leer_archivo(
        file_path
    )
    ciudades = ejemplar_tsp.get_points()
    nombre = ejemplar_tsp.get_name()
    dimension = ejemplar_tsp.get_dimension()
    copia_ciudades = []
    for ciudad in ciudades:
        copia_ciudades.append(ciudad)
    
    sol_perm = []
    while(len(copia_ciudades) > 0):
        num_aleatorio = random.randint(0,len(copia_ciudades)-1) #Es dinamico por eso funciona.
        sol_perm.append(copia_ciudades.pop(num_aleatorio))

    #Guardamos nuestra solucion aleatoria en un archivo
    with open("out_file.txt", "w") as archivo:
        archivo.write("NAME:"+nombre+"\n")
        archivo.write("DIMENSION:"+str(dimension)+"\n")
        for ciudad in sol_perm:
            archivo.write(str(ciudad[0])+" "+str(ciudad[1])+" "+str(ciudad[2])+"\n")


    distancia_max = 0.0
    primera_ciudad = 0
    segunda_ciudad = 0
    for ciudad1 in ciudades:
        for ciudad2 in ciudades:
            distancia_actual = math.sqrt(((ciudad2[1] - ciudad1[1])*(ciudad2[1] - ciudad1[1]))+ ((ciudad2[2] - ciudad1[2])*(ciudad2[2] - ciudad1[2])))
            if distancia_actual > distancia_max:
                primera_ciudad = ciudad1[0]
                segunda_ciudad = ciudad2[0]
                distancia_max = distancia_actual

    print(nombre)
    print(dimension)
    print(distancia_max)
    print(str(primera_ciudad)+" ,"+str(segunda_ciudad))
    return sol_perm

sol_aleatoria("berlin52.tsp")

"""Función para evaluar una solución aleatoria"""
def evaluar_sol(file_path): 
    ejemplar_tsp = leer_archivo(file_path)
    distancia_max = 0.0
    sol_eval = 0.0
