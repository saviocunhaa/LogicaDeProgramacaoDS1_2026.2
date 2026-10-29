
# **8. Caixa de Supermercado**
# Faça um programa para registrar os itens da compra de um cliente. O programa deve ler o preço e a quantidade de cada item continuamente. Se o preço digitado for negativo, a compra é encerrada. Se o total da compra ultrapassar R$ 200,00, o sistema deve aplicar um desconto de 10% sobre o total. Exiba o valor bruto, o valor do desconto e o valor final a pagar.


total_bruto = 0.0

print("--- Caixa do Supermercado ---")
print("Digite um preço negativo para finalizar a compra.")

while True:
    preco = float(input("Preço do item: R$ "))
    
    if preco < 0:
        break
        
    quantidade = int(input("Quantidade: "))
    
    total_bruto += (preco * quantidade)

# Calculando descontos no fim
desconto = 0.0
if total_bruto > 200.00:
    desconto = total_bruto * 0.10

total_final = total_bruto - desconto

print("\n--- Cupom Fiscal ---")
print(f"Valor Bruto: R$ {total_bruto:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a Pagar: R$ {total_final:.2f}")