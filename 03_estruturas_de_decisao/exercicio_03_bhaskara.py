"""
EXERCÍCIO 03: Fórmula de Bhaskara
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 3 valores de ponto flutuante (A, B e C) de uma equação do 2º grau.
- Se A for 0 ou delta for negativo, imprima "Impossivel calcular".
- Caso contrário, calcule e mostre as duas raízes (R1 e R2) formatadas com 5 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
A = float(input("Insira o valor de A: "))
B = float(input("Insira o valor de B: "))
C = float(input("Insira o valor de C: "))

Deltinha = B ** 2 - 4 * A * C

if A == 0 or Deltinha < 0:
    print("Impossível fazer o calculo.")
else:
    R1 = (-B + Deltinha ** 0.5) / ( 2 * A)
    R2 = (-B - Deltinha ** 0.5) / ( 2 * A)
    print(f"O Valor da primeira raiz é: {R1:.2f}")
    print(f"O Valor da segunda raiz é: {R2:.2f}")