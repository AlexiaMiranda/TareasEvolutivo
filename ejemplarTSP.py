import numpy as np
import math
#Función para leer el archivo TSP
def leer_archivo(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

        start_parsing = False
        name = ""
        dimension = 0
        coordinates=[]
        for line in lines:
            if "NAME" in line:
                name += line.split(":")[1].strip()

            if "DIMENSION" in line:
                dimension += int(line.split(":")[1].strip())

            if line.strip() == "NODE_COORD_SECTION":
                start_parsing = True
                continue
            if line.strip() == "EOF":
                break
            
            if start_parsing:
                node_x_y = line.split(" ")
                if len(node_x_y) >= 3:
                    # Extract the city number (node_x_y[0]), x-coordinate (node_x_y[1]), and y-coordinate (node_x_y[2])
                    city_number = int(node_x_y[0])
                    x_coord = float(node_x_y[1])
                    y_coord = float(node_x_y[2])
                    coordinates.append((city_number,x_coord, y_coord))#cada indice del arreglo 

        best_sol = np.zeros(dimension) # default value para la mejor solución
        act_sol = best_sol #Al inicio es la misma
        matriz_distancias = calcula_matriz(coordinates, dimension)
        tsp_element = TSP(name,coordinates, dimension, best_sol, act_sol,matriz_distancias)
    
    return tsp_element

"""Funcion que crea la matriz de distancia entre puntos"""
def calcula_matriz(ciudades, dimension):
    matriz = []
    #Inicializamos arreglos de dimension+1 con zeros, dimension + 1 para que cache 52
    for i in range(dimension+1):
        columna = np.zeros(dimension+1)
        matriz.append(columna)



    for i in range(1,dimension):
        #Suponemos que las ciudades estan en orden eg. 1...52
        city1 = ciudades[i] #recordemos que las ciudades son una lista de tripletas (id,x,y)
        id1 = city1[0] #porque iniciamos en 1 podemos mantener la correspondencia
        coord_x1 = city1[1]
        coord_y1 = city1[2]
        for j in range(1,dimension): #Es más sencillo manejarlo desde 1, para no alterar los id's de las ciudades

            city2 = ciudades[j] 
            id2= city2[0]

            coord_x2 = city2[1]
            coord_y2 = city2[2]
            distancia_actual = math.sqrt(((coord_x2 - coord_x1)*(coord_x2 - coord_x1))+ ((coord_y2 - coord_y1)*(coord_y2 - coord_y1)))
            matriz[id1][id2] = distancia_actual
            

    
            
    return matriz



#Clase para crear un ejemplar de TSP
"""Clase para crear un ejemplar de TSP
name : String : nombre del ejemplar evaluado
points: Arreglo donde points[i] corresponde a las coordenadas del nodo/punto i
dimension: Dimensión de los vectores solución
best_sol: Vector permutación que representa la mejor solución encontrada hasta el momento
act_sol: Vector de la solución activa"""
class TSP:
    def __init__(self, name, points, dimension, best_sol, act_sol, matriz_distancia):
        self.name = name
        self.points = points
        self.dimension = dimension
        self.best_sol = best_sol
        self.act_sol = act_sol
        self.matriz_distancia = matriz_distancia
    
    def get_points(self):
        return self.points
    
    def get_name(self):
        return self.name
    
    def get_dimension(self):
        return self.dimension
    
    def get_best_sol(self):
        return self.best_sol
    
    def get_act_sol(self):
        return self.act_sol
    
    def get_matriz(self):
        return self.matriz_distancia
    
# Usage
file_path = "berlin52.tsp"
city_coordinates = leer_archivo(file_path)

        
