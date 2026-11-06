"""
EXERCÍCIO 04: Casting de Dados e Idade em 2026
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba do usuário o ano de nascimento como texto (str).
Converta essa entrada para inteiro (int) utilizando o conceito de casting
e calcule a idade que a pessoa completará até o final de 2026.
Imprima a idade calculada com uma mensagem personalizada.
"""

# TODO: Desenvolva o algoritmo abaixo:

ano_nascimento_str = input("Digite o ano de seu nascimento: ")

ano_nascimento_int = int(ano_nascimento_str)
idade = 2026 - ano_nascimento_int

print(f"Até o final de 2026, sua idade será: {idade} anos!")
