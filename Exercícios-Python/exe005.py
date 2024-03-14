#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input('Digite um numero '))
print('O numero é {} seu antecessor é {} e seu sucessor é {}' .format(numero, numero-1, numero+1))