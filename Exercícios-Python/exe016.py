# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import floor

num = float(input('Digite um numero real: '))

print('O numero digitado foi {} ele inteiro é {}' .format(num, floor(num)))


# o metodo trunc foi utilizado, para cortar numeros depois da virgula e deixar o numero inteiro.
# também foi utilizado  da seguinte maneira no .format (int(num)) deixando assim o numero inteiro.