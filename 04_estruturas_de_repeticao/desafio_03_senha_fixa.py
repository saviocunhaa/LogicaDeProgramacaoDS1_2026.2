"""
DESAFIO 03: O BUG DA SENHA FIXA DO LABORATÓRIO
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
O laço de repetição do login está em loop infinito mesmo quando o usuário acerta a senha.

SUA MISSÃO:
1. Identifique por que o laço não encerra.
2. Aplique o comando adequado de quebra de fluxo (break).
"""

# CÓDIGO ORIGINAL COM LOOP INFINITO:
# senha_correta = "2002"
# while True:
#     tentativa = input("Digite a senha de acesso: ")
#     if tentativa == senha_correta:
#         print("Acesso Permitido")
#     else:
#         print("Senha Invalida")

# TODO: Escreva aqui a versão corrigida:

faturamento = float(input("Informe o faturamento anual: "))

if faturamento > 1000000:
    taxa = faturamento * 0.15
elif faturamento > 50000:
    taxa = faturamento * 0.10
elif faturamento > 0:
    taxa = faturamento * 0.05
else:
    taxa = 0.0

print(f"Taxa comercial a pagar: R$ {taxa:.2f}")

