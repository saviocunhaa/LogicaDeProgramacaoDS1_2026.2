"""
EXERCÍCIO 04: Função Lambda de Desconto Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Escreva uma função anônima (lambda) que receba o valor de um produto
e retorne o valor com 15% de desconto à vista aplicado.
"""

# TODO: Desenvolva a expressão lambda e teste-a abaixo:

desconto_a_vista = lambda valor: valor * 0.85

# Testes né pae
print(f"{desconto_a_vista(100):.2f}")
print(f"{desconto_a_vista(250):.2f}")
print(f"{desconto_a_vista(89.90):.2f}")