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



    matriz = ejemplar_tsp.get_matriz()
    distancia_max = matriz[0][0]
    ciudad_a , ciudad_b
    for i in range(1, dimension-2):
        ciudad_a = i
        for j in range (1, dimension-2):
            distancia_actual = matriz[i][j]
            if distancia_actual>distancia_max:
                distancia_max = distancia_actual
            ciudad_b = j
        

    print(nombre)
    print(dimension)
    print(distancia_max)
    print(str(ciudad_a)+" ,"+str(ciudad_b))
    return sol_perm

sol_aleatoria("berlin52.tsp")

"""Función para evaluar una solución aleatoria"""
def evaluar_sol(file_path): 
    ejemplar_tsp = TSP(file_path)
    matriz = ejemplar_tsp.get_matriz()

    sol_aleatoria = sol_aleatoria(file_path)
    sol_eval = 0.0

    for i in range(len(sol_aleatoria)-2):
        ciudad_i = sol_aleatoria[i]
        ciudad_j = sol_aleatoria[i+1]
        distancia_ij = matriz[ciudad_i][ciudad_j]
        sol_eval = sol_eval+distancia_ij

    return sol_eval


        

