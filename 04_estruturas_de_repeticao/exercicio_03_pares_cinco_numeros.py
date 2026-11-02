"""
EXERCÍCIO 03: Pares entre Cinco Números
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite 5 números inteiros ao usuário.
Utilize uma estrutura de repetição e um contador para verificar quantos números pares
foram digitados. Ao final, imprima a quantidade total.
"""

# TODO: Desenvolva o algoritmo abaixo:

print(" Um total de cinco números inteiros serão necessários!")

contador_de_pares = 0 

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero % 2 == 0:
        contador_de_pares += 1

print(f"A quantidade de números pares no digitados: {contador_de_pares}")