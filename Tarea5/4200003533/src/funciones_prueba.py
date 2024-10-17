import numpy as np

"""Funcion sphere"""
def sphere(vector):
    suma = 0
    for xi in vector:
        cuadrado = xi * xi
        suma += cuadrado
    return suma

def ackley(vector):
    d = len(vector)  # Dimensión del vector
    raiz_suma = 0
    cos_suma = 0
    for i in range(1,d):
        xi = vector[i]
        raiz_suma += xi * xi
        np.cos(2 * np.pi * xi)

    sum_term = 20 + 2.71828 - 20 * np.exp(-0.2 * np.sqrt(raiz_suma/ d))
    cos_term = -np.exp(cos_suma / d)
    return sum_term + cos_term

def griewank(vector):
    d = len(vector) 
    raiz_suma = 0
    cos_prod = 1
    for i in range(1,d):
        xi = vector[i]
        raiz_suma += xi * xi
        cos_prod = cos_prod * np.cos(xi/np.sqrt(i))

    raiz_suma = raiz_suma/4000 

    return raiz_suma + cos_prod

def cuadrado_vector(vector):
    suma = 0
    for xi in vector:
        cuadrado = xi * xi
        suma += cuadrado
    return suma

def rastrigin(vector):
    d = len(vector)  # Dimensión del vector
    suma_term = 0
    for xi in vector:
        cuadrado = xi * xi
        resta = -10* np.cos(2*np.pi * xi)
        suma_term += cuadrado + resta

    return 10 * d + suma_term

def rosenbrock(vector):
    d = len(vector)
    suma = 0
    for i in range (1, d-1):
        xi = vector[i]
        xi1 = vector[i+1]
        cuadrado = xi * xi
        resta1 = xi1 - cuadrado
        true_resta1 = resta1 * resta1
        resta2 = 1-xi
        true_resta2 = resta2 * resta2
        suma += 100* true_resta1 + true_resta2

    return suma
    

