"""
DESAFIO 04: REFATORAÇÃO INVESTIGATIVA
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
O código monolítico repete cálculos de desconto e impostos várias vezes.

SUA MISSÃO:
1. Crie uma função calcular_preco_final(preco_base, taxa_desc, taxa_imp) com return.
2. Crie um procedimento exibir_relatorio_item(numero_item, preco_final) com print.
3. Teste suas funções refatoradas.
"""

# TODO: Desenvolva as funções modulares abaixo:

def gerar_relatorio_produto(nome, custo, venda):
    lucro = venda - custo
    print("-" * 30)
    print(f"Produto: {nome}")
    print(f"Custo: R$ {custo:.2f}")
    print(f"Venda: R$ {venda:.2f}")
    print(f"Lucro Líquido: R$ {lucro:.2f}")
    print("-" * 30)

gerar_relatorio_produto("Teclado Gamer", 80.00, 150.00)

