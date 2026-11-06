"""
EXERCÍCIO 03: Conta do Nagoya Sushi House
Disciplina: Lógica de Programação com Python
ENUNCIADO:
Crie um programa que:
1. Leia o valor total consumido no restaurante (em R$).
2. Aplique a taxa de 10% de serviço do garçom.
3. Exiba o valor final da conta a pagar com mensagem formatada.
"""

# TODO: Desenvolva o algoritmo abaixo:

valor_consumido = float(input("Digite o valor consumido (R$): "))

taxa_garcom = valor_consumido * 0.10
valor_final = valor_consumido + taxa_garcom

print(f"Valor final da conta com taxa de 10%: R$ {valor_final:.2f}")
