"""
EXERCÍCIO 02: Aumento de Salário Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de um colaborador da escola e aplique o percentual de reajuste:
- 0.00 a 400.00: 15%
- 400.01 a 800.00: 12%
- 800.01 a 1200.00: 10%
- 1200.01 a 2000.00: 7%
- Acima de 2000.00: 4%

Imprima: novo salário, valor do reajuste ganho e percentual aplicado.
"""

# TODO: Desenvolva o algoritmo abaixo:
 
salario = float(input("Coloque o valor do salário: R$"))
if salario <= 400.00:
    percentual = 15
elif salario <=800.00:
    percentual = 12
elif salario <= 1200.00:
    percentual = 10
elif salario <= 2000.00:
    percentual = 7
else:
    percentual = 4

novoSalario = salario + (salario * percentual / 100)
reajuste = novoSalario - salario
print(f"O Novo salário do colaborador é de: R${novoSalario:.2f}")
print(f"O valor do reajuste no salário do colaborador foi de: R${reajuste:.2f}")
print(f"O percentual aplicado no salário do contribuinte foi de: {percentual}%")