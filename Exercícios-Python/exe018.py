# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

angulo = float(input('Digite o Angulo que você deseja: '))

import math

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('Se o angulo é {:.2f} o Seno é {:.2f}, o Cosseno é {:.2f} e a tangente é {:.2f}'
       .format(angulo, seno, cosseno, tangente))

# a biblioteca informa que para identificar Sen, Cos e Tan o angulo precisa ficar em radiano.
# ChatGPT recomendou alteração do angulo para radianos, assim ficaria mais simples identificar o Sen, Cos e Tan;

