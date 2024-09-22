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
        archivo.write("NODE_COORD_SECTION\n")
        for ciudad in sol_perm:
            archivo.write(str(ciudad[0])+" "+str(ciudad[1])+" "+str(ciudad[2])+"\n")


    #Lo convertimos en un ejemplar de tsp
    ejemplar_sol_aleatoria = leer_archivo("out_file.txt")
    matriz = ejemplar_sol_aleatoria.get_matriz()
    #Calculamos la distancia maxima

    distancia_max=0
    k = 0
    r = 0
    for i in range(1,dimension):
        k=i
        for j in range (1,dimension):
            r = j
            distancia_actual = matriz[i][j]
            if distancia_actual>distancia_max:
                distancia_max = distancia_actual
            

    print(ejemplar_sol_aleatoria.get_name())
    print(ejemplar_sol_aleatoria.get_dimension())
    print(distancia_max)
    print(str(k)+" ,"+str(r))
    return ejemplar_sol_aleatoria

"""Función para evaluar una solución aleatoria"""
def evaluar_sol_aleatoria(file_path): 
    
    #Obtenemos una solución aleatoria
    ejemplar_sol = sol_aleatoria(file_path)
    sol = ejemplar_sol.get_points() #Nos devuelve una lista con los nodos y sus coordenadas
    dimension = ejemplar_sol.get_dimension()
    matriz = ejemplar_sol.get_matriz()
    sol_eval = 0.0

    for i in range(1,dimension-1):
        ciudad_i = sol[i][0] #para obtener el id de la ciudad donde estamos parados
        ciudad_j = sol[i+1][0]
        distancia_ij = matriz[ciudad_i][ciudad_j]
        sol_eval = sol_eval+distancia_ij
    print(len(sol))
    print("Costo de la solución: "+ str(sol_eval))
    return sol_eval

evaluar_sol_aleatoria("berlin52.tsp")
        

