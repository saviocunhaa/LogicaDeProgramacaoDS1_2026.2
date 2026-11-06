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

valor_investido = float(input("Digite o valor investido (R$): "))
cliques = int(input("Digite o total de cliques: "))

cpc = valor_investido / cliques

print(f"Custo Por Clique (CPC) médio: R$ {cpc:.2f}")
