# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome completo: ")).strip()

# a utilização do STRIP deve ser no recebimento de dados

print("O seu nome maiusculo é: {}" .format(nome.upper()))
print("O seu nome minusculo é: {}" .format(nome.lower()))
print("A quantidade de caracteres é: {}" .format(len(nome) - nome.count(" ")))
print("o seu primeiro nome tem {} letras" .format(nome.find(" ")))

