# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Digite a quantidade de Metros: '))

cm = metros*100
mm = cm*10
micro = mm*1000



print('o valor em Metros é {}, em Centimetros é {}, em milímetros é {} e o valor em micrômetros é {}'.format(metros, cm, mm, micro) )