# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.

import math
#from math import hypot

coposto = float(input('Digite o comprimento do cateto oposto: '))
cadjacente = float(input('Digite o comprimento do cateto adjascente: '))

hipotenusa = math.pow(coposto, 2) + math.pow(cadjacente, 2)

print('A hiponetusa vai medir: {:.2f}' .format(math.sqrt(hipotenusa))) 

# foi utilizado o metodo math.hypot(coposto, cadjacente) onde implementamos apenas os catetos
