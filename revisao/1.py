# **1. Calculadora de Frete de E-commerce**
# Uma loja virtual precisa de um sistema para calcular o valor do frete. Crie uma função que receba a distância em quilômetros e o tipo de cliente ("Padrão" ou "VIP"). A regra é: R$ 0,50 por km rodado. Se a distância for maior que 100 km, há uma taxa fixa adicional de R$ 15,00. Clientes VIP recebem 20% de desconto no valor final do frete. Peça para o usuário inserir os dados e exiba o resultado utilizando a função criada.


def calcular_frete(distancia, tipo_cliente):
    # Cálculo base: R$ 0,50 por km
    valor = distancia * 0.50
    
    # Taxa adicional se a distância for maior que 100km
    if distancia > 100:
        valor += 15.00
        
    # Aplicação de desconto para VIPs
    # O método .upper() garante que "vip", "Vip" ou "VIP" funcionem
    if tipo_cliente.upper() == "VIP":
        valor = valor * 0.80  # Dá 20% de desconto (cobra 80% do valor)
        
    return valor

# Programa Principal
print("--- Calculadora de Frete ---")
dist_km = float(input("Informe a distância em km: "))
cliente = input("Qual o tipo de cliente (Padrão ou VIP)? ")

frete_final = calcular_frete(dist_km, cliente)
print(f"O valor final do frete é: R$ {frete_final:.2f}")