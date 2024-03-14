# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o seu salario: R$'))

aumento = salario * 0.15

if salario > 1250:
    aumento = salario * 0.1
    
print('Seu salario atual é R${}, com o aumento fica R${}' .format(salario, salario+aumento)) 
# o print precisa estar fora do IF para o funcionamento da mesma variavel