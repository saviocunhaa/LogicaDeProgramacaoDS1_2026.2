# **6. Sistema de Tarifas de Táxi**
# Crie duas funções distintas: `tarifa_diurna(distancia)` e `tarifa_noturna(distancia)`. A tarifa diurna cobra R$ 4,00 de bandeirada mais R$ 2,50 por km. A noturna cobra R$ 6,00 de bandeirada mais R$ 3,20 por km. O programa principal deve usar um laço para atender vários passageiros ao longo do turno de um motorista. Para cada passageiro, pergunte se a corrida foi de dia (D) ou de noite (N) e a distância. Chame a função adequada e some o valor para o caixa do motorista. O turno acaba quando a distância informada for negativa.

def tarifa_diurna(distancia):
    return 4.00 + (2.50 * distancia)

def tarifa_noturna(distancia):
    return 6.00 + (3.20 * distancia)

caixa_motorista = 0.0

print("--- Sistema do Taxista ---")
print("Digite uma distância negativa para encerrar o turno.")

while True:
    dist = float(input("\nDistância da corrida (km): "))
    
    if dist < 0:
        break
        
    turno = input("Turno: (D) Dia ou (N) Noite? ").upper()
    
    if turno == "D":
        valor_corrida = tarifa_diurna(dist)
        caixa_motorista += valor_corrida
        print(f"Valor cobrado: R$ {valor_corrida:.2f}")
    elif turno == "N":
        valor_corrida = tarifa_noturna(dist)
        caixa_motorista += valor_corrida
        print(f"Valor cobrado: R$ {valor_corrida:.2f}")
    else:
        print("Turno inválido. Corrida não registrada.")

print(f"\nTurno encerrado. Caixa total do motorista: R$ {caixa_motorista:.2f}")