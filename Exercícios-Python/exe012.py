#  Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Informe o valor do Produto R$'))

desconto = produto * 0.05

print('O valor do seu produto é {} com desconto fica {}' .format(produto, produto-desconto))

#a resolução foi uma multiplicação e uma divisão por 100
# ficaria um produto de 10 reais multiplicado por 5 e dividido por 100 dando asssim 5% de desconto (R$9,50)