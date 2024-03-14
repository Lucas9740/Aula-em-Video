# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

kilometros = float(input('Qual a distancia da sua viagem, em KM? '))

if kilometros > 200:
    v1 = kilometros * 0.45
    print('o valor da sua viagem é: {}' .format(v1))
else:
    v2 = kilometros * 0.50
    print('O valor da sua viagem é: {}' .format(v2))


# na resolução do exercício foi utilizado apenas uma variavel para representar o valor