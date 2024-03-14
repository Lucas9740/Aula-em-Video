# Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

lag = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))

area = lag*alt
qt_tinta = area/2

print('Se a parede possui {} de largura e {} de altura \n'
      'então sua area é {} e a quantidade de tinta em litros é {}' .format(lag, alt, area, qt_tinta))
