# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
from random import shuffle

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]
print('A ordem sorteada é: {}' .format(random.sample(lista, 4)))


# busquei na biblioteca random a utilização do random.sample, onde posso sortear um ou mais nomes a 
# partir da list. Ao colocar a quantidade de nomes a serem sorteados, a função identifica 4 como quantidade e não 3
# na lista o 4 é identificado como 4, não começa do zero
#ChatGPT mostrou a mesma função sample.

# a explicação na resolução do exercício não foi utilizado a função sample, mas sim shuffle

# lista = [aluno1, aluno2, aluno3, aluno4]
# print('A ordem sorteada é: {}' .format(random.shuffle(lista))