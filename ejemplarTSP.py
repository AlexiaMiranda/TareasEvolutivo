import numpy as np
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
        tsp_element = TSP(name,coordinates, dimension, best_sol, act_sol)
    
    return tsp_element

#Clase para crear un ejemplar de TSP
"""Clase para crear un ejemplar de TSP
name : String : nombre del ejemplar evaluado
points: Arreglo donde points[i] corresponde a las coordenadas del nodo/punto i
dimension: Dimensión de los vectores solución
best_sol: Vector permutación que representa la mejor solución encontrada hasta el momento
act_sol: Vector de la solución activa"""
class TSP:
    def __init__(self, name, points, dimension, best_sol, act_sol):
        self.name = name
        self.points = points
        self.dimension = dimension
        self.best_sol = best_sol
        self.act_sol = act_sol
    
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
    
# Usage
file_path = "berlin52.tsp"
city_coordinates = leer_archivo(file_path)
print(city_coordinates.get_points())
