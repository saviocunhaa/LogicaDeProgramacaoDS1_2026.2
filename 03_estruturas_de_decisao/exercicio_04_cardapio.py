"""
EXERCÍCIO 04: Cardápio da Lanchonete
Disciplina: Lógica de Programação com Python

TABELA:
1 - Cachorro Quente: R$ 4.00
2 - X-Salada: R$ 4.50
3 - X-Bacon: R$ 5.00
4 - Torrada Simples: R$ 2.00
5 - Refrigerante: R$ 1.50

ENUNCIADO:
Leia o código do item e a quantidade consumida.
Calcule e mostre o total a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
codigo = int(input("Por favor, insira o código do produto: "))
quantidade = int(input("Por favor, insira a quantidade consumida: "))
if codigo == 5:
    preco = 1.50
elif codigo == 4:
    preco = 2.00
elif codigo == 3:
    preco = 5.00
elif codigo == 2:
    preco = 4.50
elif codigo == 1:
    preco = 4.00

else:
    print("Código não encontrado")
    exit()

totalapagar = preco * quantidade
print(f"O Valor total a se pagar é de: R${totalapagar:.2f}")