"""
EXERCÍCIO 01: Gestão de Tráfego Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
A loja Casas Paulino está veiculando anúncios no Meta Ads em Tianguá.
Escreva um programa que leia:
1. O valor total investido na campanha (em R$).
2. O número total de cliques obtidos.

Calcule e mostre na tela o Custo Por Clique (CPC) médio da campanha formatado em reais.
"""

# TODO: Desenvolva o algoritmo abaixo:

# o programa quer que eu faça ele ler um valor investido, ou seja um número float, em seguida leia outro falor inteiro que seria
# o valor por cliques e em seguida dividir um pelo outro, sendo uma média básica e formatar em reais com casas decimais?

valorInvestido = float(input("Insira o valor investido em anúncios na cidade de Tianguá: R$"))
numeroDeCliquesObtidos = int(input("Insira o valor de Cliques obtidos: "))
cpc = valorInvestido / numeroDeCliquesObtidos
print(f"O cusco por clique (CPC) foi de: R${cpc:.1f}")