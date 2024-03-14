# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Digite quanto em reais você possui: R$'))

dolar = real/4.95

print('Você possui R${} e ${:.2f}' .format(real, dolar))