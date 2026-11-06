"""
EXERCÍCIO 04: Função Lambda de Desconto Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Escreva uma função anônima (lambda) que receba o valor de um produto
e retorne o valor com 15% de desconto à vista aplicado.
"""

# TODO: Desenvolva a expressão lambda e teste-a abaixo:

calcular_desconto = lambda valor: valor * 0.85

preco_com_desconto = calcular_desconto(100.00)
print(f"Preço final com 15% de desconto: R$ {preco_com_desconto:.2f}")

