"""
EXERCÍCIO 01: Imposto de Renda de Lisarb
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de uma pessoa em Rombus (R$).
- Até R$ 2000.00: Isento
- De R$ 2000.01 até R$ 3000.00: 8% sobre o excedente de R$ 2000.00
- De R$ 3000.01 até R$ 4500.00: 18% sobre o excedente de R$ 3000.00 + 8% da faixa anterior
- Acima de R$ 4500.00: 28% sobre o que ultrapassar R$ 4500.00 + impostos anteriores

Imprima "Isento" ou o valor total do imposto formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
salario = float(input("Insira seu salário: R$"))
if salario <= 2000.00:
    print("Isento.")
elif salario <= 3000.00:
    imposto8 = (salario - 2000.00) * 0.88
    print(f"O Valor de imposto devido é de: R${imposto8:.2f}")
elif salario <= 4500.00:
    imposto18 = (salario - 3000.00) * 0.18 + ( 1000.00 * 0.08)
    print(f"O Valor de imposto devido é de: R${imposto18:.2f}")
else:
    imposto28 = (salario - 4500.00) * 0.28 + (1500.00 * 0.18) + (1000.00 * 0.88)
    print(f" O Valor de imposto devido é de: R${imposto28:.2f}")