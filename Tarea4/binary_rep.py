import numpy as np

def to_binary(n, nBit):
    # Mayor número a representar:
    max_dec = (2 ** nBit) - 1
    binary = bin(n)[2:]  # Conversión a binario y eliminación del prefijo '0b'
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
def real_binary(x, nBit, a, b):
    num_inter = 2 ** nBit  # Número de intervalos posibles
    dist_ab = b - a  # Intervalo para la partición uniforme
    delta = dist_ab / num_inter  # Delta para mantener uniforme la partición
    real_intervalo = x - a
    real_cod = int(real_intervalo / delta)
    return to_binary(real_cod, nBit)

def decode_nat(nat):
    print(nat)
    nBits = len(nat)
    
    # Revertir la cadena
    nat_reverse = nat[::-1]
    
    suma = 0
    for i in range(nBits):  # Recorre la cadena de derecha a izquierda
        if nat_reverse[i] == '1':
            suma += 2 ** i
    
    return suma

def decodifica_real(real_binary, a, b):
    # Signo del exponente
    if real_binary[0] == '0':
        exp_sin = "-"
    else:
        exp_sin = "+"
    
    # Parte del exponente decodificada
    exp_bin = real_binary[1:4]
    nat_exp = exp_sin + str(decode_nat(exp_bin))  # Llama a la función decode_nat previamente definida

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
    ent_body = decode_nat(ent)
    real_ent = str(a + (ent_body * delta))

    # Combina las partes
    real = nat_exp + ent_sin + real_ent
    return real
