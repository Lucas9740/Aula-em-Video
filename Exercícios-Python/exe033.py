# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('digite um valor: '))
n2 = int(input('digite outro valor: '))
n3 = int(input('digite mais um valor: '))

# verifica o menor
menor = n1
if n2<n1 and n2<n3 :
    menor = n2
if n3<n1 and n3<n2 :
    menor = n3
print(' o menor valor digitado é: ' .format(menor))
maior = n1
if n2>n1 and n2>n3 :
    maior = n2
if n3>n1 and n3>n2 :
    maior = n3
    