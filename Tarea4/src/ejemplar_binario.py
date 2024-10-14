import numpy as np
import random
import funciones_prueba

class Individuo:
    def __init__(self, id, vector, dimension, fitness):
        self.id = id
        self.vector = vector
        self.dimension = dimension
        self.fitness = fitness

    def get_vector(self):
        return self.vector
    
    def get_id(self):
        return self.name
    
    def get_dimension(self):
        return self.dimension
    
    def get_fitness(self):
        return self.fitness
    
    def copy(self):
        id = self.id
        vector = []
        for cromosoma in self.vector:
            vector.append(cromosoma)

        dimension = self.dimension
        fitness = self.fitness
        neo_individuo = Individuo(id, vector, dimension, fitness)
        return neo_individuo

class Poblacion:
    """
    Método para inicializar la poblacion.

    Args:
        - dimension: Tamaño de los vectores. Dependiendo de la función con la que probemos es que limitamos la cantidad maxima a representar.
        - num_individuos: La cantidad de individuos para la población.
        - num_iteraciones: Número de iteraciones maximas.
        - limit_a: Limite inferior del dominio.
        - limit_b: Limite superior del dominio.
        - funcion: String que define la función de prueba sobre la que se aplicará la poblacion.

    Return: Población.
    """
    def __init__(self, dimension, num_individuos, limit_a, limit_b, funcion):
        individuos = []
        for i in range(num_individuos):
            vector_i = self.generar_aleatoria_01(dimension, limit_a, limit_b)
            fitness = self.calcular_fitness_maximizar(vector_i, funcion)
            individuo_i = Individuo(i, vector_i, dimension, 0) #Si hay que hacer el fitness

            individuos.append(individuo_i)
        self.individuos = individuos
        self.dimension = dimension
        self.num_individuos = num_individuos  
        #self.mejor_individuo = None  
            

    """
    Método generar una solución aleatoria binaria en un rango permitido:

    Args:
        - dimension: Dimension del vector con este determinaremos el número de bits.
        - limit_a: Limite inferior
        - limit_b: Limite superior
    Return: Un vector en binario representando un número real."""
    def generar_aleatoria_01(self, dimension, limit_a, limit_b):
        real = random.uniform(limit_a, limit_b+0.1) 
        real_binary = real_binary(real,dimension, limit_a, limit_b)
        return real_binary


    """
    Método auxiliar para calcular el fitness de un individuo:

    Args:
        - vector: vector al que le calcularemos la funcion fitness.
        - funcion: string que indica la funcion sobre el calcularemos el fitness

    Return: El valor del fitness."""
    def calcular_fitness_maximizar(self, vector, funcion:str):
        result:int
        if funcion == "sphere":
            result = funciones_prueba.sphere(vector)
        elif funcion == "ackley":
            result = funciones_prueba.ackley(vector)
        elif funcion == "griewank":
            result = funciones_prueba.griewank(vector)
        elif funcion == "rastrigin":
            result = funciones_prueba.rastrigin(vector)
        elif funcion == "rosenbrock":
            result = funciones_prueba.rosenbrock(vector)
        else:
            print("No función definida")
        return result

    def calcular_fitness_minimizar(self, vector, funcion:str):
        result:int
        if funcion == "sphere":
            result = - funciones_prueba.sphere(vector)
        elif funcion == "ackley":
            result = - funciones_prueba.ackley(vector)
        elif funcion == "griewank":
            result = - funciones_prueba.griewank(vector)
        elif funcion == "rastrigin":
            result = - funciones_prueba.rastrigin(vector)
        elif funcion == "rosenbrock":
            result = - funciones_prueba.rosenbrock(vector)
        else:
            print("No función definida")
        return result

    def to_binary(self,n, nBit):
        # Mayor número a representar:
        max_dec = (2 ** nBit) - 1
        binary = bin(n)
        len_binary = len(binary)

        if len_binary == nBit:
            return binary

        if len_binary < nBit:
            dif = nBit - len_binary
            zero = "0" * dif
            final_binary = zero + binary
            return final_binary

        print(f"El máximo número a representar es: {max_dec}")
        return ""

    # Método para codificar números reales, tomando en cuenta que la partición es uniforme sobre un intervalo [a, b]
    def real_binary(self,x, nBit, a, b):
        num_inter = 2 ** nBit  # Número de intervalos posibles
        dist_ab = b - a  # Intervalo para la partición uniforme
        delta = dist_ab / num_inter  # Delta para mantener uniforme la partición
        real_intervalo = x - a
        real_cod = int(real_intervalo / delta)
        return self.to_binary(real_cod, nBit)

    def decode_nat(self,nat):
        print(nat)
        nBits = len(nat)

        # Revertir la cadena
        nat_reverse = nat[::-1]

        suma = 0
        for i in range(nBits):  # Recorre la cadena de derecha a izquierda
            if nat_reverse[i] == '1':
                suma += 2 ** i

        return suma

    def decodifica_real(self, real_binary, a, b):
        # Signo del exponente
        if real_binary[0] == '0':
            exp_sin = "-"
        else:
            exp_sin = "+"

        # Parte del exponente decodificada
        exp_bin = real_binary[1:4]
        nat_exp = exp_sin + str(self.decode_nat(exp_bin))  # Llama a la función decode_nat previamente definida

        # Signo del entero
        if real_binary[4] == '0':
            ent_sin = "-"
        else:
            ent_sin = "+"

        nBits = len(real_binary)
        ent = real_binary[5:nBits]  # Extrae la parte del entero

        num_inter = 2 ** nBits  # Número de intervalos posibles
        distanciaAB = b - a
        delta = distanciaAB / num_inter

        # Reconstruye el valor real
        ent_body = self.decode_nat(ent)
        real_ent = str(a + (ent_body * delta))

        # Combina las partes
        real = nat_exp + ent_sin + real_ent
        return real
