"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:

positivos = 0
soma = 0.0

for i in range(6):
    numero = float(input(f"Digite o {i+1}º número: "))
    if numero > 0:
        positivos += 1
        soma += numero

print(f"{positivos} valores positivos")
if positivos > 0:
    media = soma / positivos
    print(f"{media:.1f}")

