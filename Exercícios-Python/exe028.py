# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça 
# para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá 
# escrever na tela se o usuário venceu ou perdeu.

from random import randint #gerador de numero aleatorio entre 0 e 5
from time import sleep  # gera um tempo até o proximo comando
computador = randint(0, 5)  
print('Tente adivinhar o numero que pensei, entre 0 e 5!')
numero = int(input('Em que numero eu pensei?')) # tentativa do usuário
print('Processando...')
sleep(3)

if computador == numero:
    print('Parabens! você acertou')
else:
    print('Errou! pensei em numero {} e não {}' .format(computador, numero))

