import numpy as np
import random
from ejemplar_binario import Poblacion, Individuo

"""
    Selección de padres usando el método de la ruleta.
    
    Args:
    - population: lista de individuos.
    - num_seleccionados: número de padres a seleccionar.
        
    Return: Lista de individuos seleccionados.
"""
def seleccion_ruleta(population, num_seleccionados):
    # Convertir los valores de fitness en probabilidades sumando al total
    probabilidades = []
    for individuo in population:
        fitness = individuo.get_fitness()
        total_fitness = sum(fitness) #el fitness total
        probabilidades.append(fitness/total_fitness)
    
    # Usar np.random.choice para seleccionar según las probabilidades.
    #Generamos el mismo numero de hijos para que sean la misma cantidad que el de los padres.
    seleccionados_indices = np.random.choice(len(population), size=num_seleccionados, replace=True, p=probabilidades)
    
    # Devolver los individuos seleccionados
    seleccionados = []
    for i in seleccionados_indices:
        seleccionados.append(population[i])

    return seleccionados



"""
Operador de cruza de n puntos. Método que recibe dos padres y n puntos donde cortar y combinar

Args:
- padre1: Representación del ejemplar padre1.
- padre2: Representación del ejemplar padre2.
- n_puntos: Número de puntos de cruce a utilizar.

Return: hijo1, hijo2: Dos hijos resultantes de la cruza.
"""
def cruza_n_puntos(padre1:Individuo, padre2:Individuo, n_puntos):

    if len(padre1) != len(padre2):
        raise ValueError("Ambos padres deben tener la misma longitud.")

    #Ahora si obtenemos la dimension
    longitud = padre1.get_dimension()
    
    # Generar puntos de cruce aleatorios, asegurándonos que no haya duplicados y estén en orden
    puntos_cruce = sorted(random.sample(range(1, longitud), n_puntos))

    # Inicializar los hijos con los padres originales
    hijo1 = list(padre1)
    hijo2 = list(padre2)
    
    # Alternar segmentos entre los puntos de cruce
    for i in range(len(puntos_cruce)):
        if i % 2 == 0:  # Si el índice es par, intercambiar segmentos, es la forma más sencilla
            inicio = puntos_cruce[i]
            fin = puntos_cruce[i+1] if i+1 < len(puntos_cruce) else longitud
            
            # Intercambiar entre padre1 y padre2
            hijo1[inicio:fin], hijo2[inicio:fin] = hijo2[inicio:fin], hijo1[inicio:fin]
    
    return (hijo1,hijo2)  # regresamos una tupla con ambos hijos


import random

"""
    Aplica mutación flip a un individuo.
    
    Args:
    individuo: representación de un individuo.
    
    Returns: Un nuevo individuo con mutación.
    """
def mutacion_flip(individuo, tasa_m): 
    
    neo_individuo = individuo.copy()  # Copia del individuo original
    for i in range(len(individuo)):
        if random.random() < tasa_m: #Para que sea justo
            # Invertimos el bit (de 0 a 1, o de 1 a 0)
            if individuo[i] == 0 :
                neo_individuo[i] = 1 
            else:
                0
    return neo_individuo




    

"""
    Selecciona los mejores individuos (elitistas) según su valor de fitness.
    
    Args:
    - poblacion: lista de individuos.
    - num_elitistas: número de individuos elitistas a seleccionar.
    
    Return: Lista de los individuos elitistas seleccionados.
"""
def seleccionar_elitistas(poblacion, num_elitistas):
    fitness = []
    for individuo in poblacion:
        fit = individuo.fitness
        fitness.append(fit)
    # Combina población con sus valores de fitness
    individuos_con_fitness = list(zip(poblacion, fitness))
    # Ordena por fitness en orden descendente (mejor fitness primero)
    individuos_con_fitness.sort(key=lambda x: x[1], reverse=True)
    # Devuelve los mejores 'num_elitistas' individuos
    elite = []
    for individuo, _ in individuos_con_fitness[:num_elitistas]:
        elite.append(individuo)

    return elite #regresa una lista de tuplas con los mejores individuos y sus respectivos fitness
"""
    Crea siguiente generación elitista.
    
    Args:
    - poblacion: lista de individuos.
    - num_elite: número de individuos elitistas a seleccionar.
    
    Return: Siguiente generacion.
"""

def siguiente_generacion(poblacion:Poblacion, num_elite):
    num_individuos = len(poblacion)
    fijos = seleccionar_elitistas(poblacion, num_elite)
    num_hijos = num_individuos - num_elite
    padres = seleccion_ruleta(poblacion, num_hijos)
    next_gen = [] 
    for i in range(num_hijos-2):
        padre1_i = padres[i]
        padre2_i = padres[i+1]
        dimension = poblacion.dimension
        n_puntos = random.uniform(0, dimension-1)
        hijos = cruza_n_puntos(padre1_i, padre2_i, n_puntos)
        for j in range(2):
            hijo = hijos[j]
            hijo_m = mutacion_flip(hijo, 0.4) #le aplicamos una mutación baja
            next_gen.append(hijo_m)

    for elite in fijos:
        next_gen.append(elite)
    

    
        



