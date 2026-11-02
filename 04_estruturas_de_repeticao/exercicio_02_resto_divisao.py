"""
EXERCÍCIO 02: Resto da Divisão por 5
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia dois valores inteiros X e Y.
Utilize o laço for para imprimir todos os inteiros entre X e Y (em ordem crescente)
cujo resto da divisão por 5 seja igual a 2 ou igual a 3.
"""

# TODO: Desenvolva o algoritmo abaixo:

x = int(input("Insira o primeiro valor!:"))
y = int(input("Insira o segundo valor!:"))
for numero in range(x,y,+1):
    if numero % 5 == 2 or numero % 5 == 3:
        print(numero)