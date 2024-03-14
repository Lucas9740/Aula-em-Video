# Faça um programa que leia algo pelo teclado e mostre na tela 
#  o seu tipo primitivo e todas as informações possíveis sobre ele.
 
a = input("Digite algo: ")

print("O tipo primitivo desse valor é: ", type(a))
print("É um número: ", a.isnumeric())
print("É alfabético: ", a.isalpha())
print("É alfanumerico: ", a.isalnum())
print("esta em maiusculo: ", a.isupper())
print("esta em minusculo: ", a.islower())
print("esta em titulo: ", a.istitle())
