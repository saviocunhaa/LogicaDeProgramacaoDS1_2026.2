"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:

def calcular_pontuacao_total(fase1, fase2, fase3):
    return fase1 + fase2 + fase3

resultado = calcular_pontuacao_total(80, 90, 100)
print(f"Pontuação Total da Equipe: {resultado} pontos")

