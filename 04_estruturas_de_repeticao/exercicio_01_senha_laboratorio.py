"""
EXERCÍCIO 01: Senha Fixa do Laboratório
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Repita a leitura da senha até que o usuário digite a senha correta (2002).
Para cada tentativa incorreta, imprima "Senha Invalida".
Ao acertar, imprima "Acesso Permitido" e finalize o programa.
"""

# TODO: Desenvolva o algoritmo abaixo:

correct_pass = "2002"

while True:
    tentativa = input("Insira a senha de acesso: ")
    if tentativa == correct_pass:
        print("Acesso Garantido!")
        break
    else:
        print("Acesso Negado! Senha incorreta.")