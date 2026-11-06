"""
EXERCÍCIO 05: Acesso à Bilheteria do Parque
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba a idade do visitante (valor base do ingresso: R$ 100,00):
- Menor que 12 anos: "Infantil" (50% de desconto -> R$ 50,00)
- Maior ou igual a 60 anos: "Melhor Idade" (Gratuidade -> R$ 0,00)
- Demais idades: "Integral" (R$ 100,00)

Imprima o tipo de bilhete e o valor final a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:

idade = int(input("Digite a idade do visitante: "))

if idade < 12:
    tipo = "Infantil"
    valor = 50.00
elif idade >= 60:
    tipo = "Melhor Idade"
    valor = 0.00
else:
    tipo = "Integral"
    valor = 100.00

print(f"Tipo de bilhete: {tipo}")
print(f"Valor final a pagar: R$ {valor:.2f}")

