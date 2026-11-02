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

def calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel):
    litros = distancia_km / consumo_kml
    return litros * preco_combustivel


def calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao):
    return qtd_pessoas * dias * diaria_alimentacao

distancia = float(input("Distância total da viagem (km): "))
consumo = float(input("Consumo do veículo (km por litro): "))
preco = float(input("Preço do combustível (R$ por litro): "))
pessoas = int(input("Quantidade de pessoas: "))
dias = int(input("Quantidade de dias: "))
diaria = float(input("Gasto diário com alimentação por pessoa (R$): "))

custo_transporte = calcular_custo_transporte(distancia, consumo, preco)
custo_alimentacao = calcular_custo_alimentacao(pessoas, dias, diaria)
custo_total = custo_transporte + custo_alimentacao

print(f"Custo de transporte: R${custo_transporte:.2f}")
print(f"Custo de alimentação: R${custo_alimentacao:.2f}")
print(f"Custo total da viagem: R${custo_total:.2f}")