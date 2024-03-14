# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

ano = int(input('Que ano quer analisar? digite 0 para analisar o ano atual'))

if ano == 0:
    ano = date.today().year     # importa a data atual do computador, se o usuário digitar 0 ela é selecionada
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('Ano {} é Bissexto' .format(ano))
    else:
        print('Ano {} não é Bissexto' .format(ano))