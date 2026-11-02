"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:

print("Você terá que digitar seis valores!")

contadordePositivos = 0
soma_positivos = 0

for i in range(6):
    valores = float(input(f"Digite o {i+1}º valor: "))
if contadordePositivos > 0:
    media = soma_positivos / contadordePositivos 
    print(f"Média: {media:.1f}")
else:
    print("Nenhum valor positivo foi digitado")