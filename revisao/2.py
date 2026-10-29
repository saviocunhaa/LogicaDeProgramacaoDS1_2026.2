
# **2. Monitoramento de Temperatura em Estufa**
# Um agricultor possui uma estufa e um sensor de temperatura que faz leituras constantes. Escreva um programa que leia continuamente a temperatura registrada (em graus Celsius) até que o usuário digite um valor de parada (por exemplo, -99). Ao final, o programa deve exibir:
# * A temperatura média do período.
# * Quantas vezes a temperatura ultrapassou a marca de perigo (acima de 35°C).


soma_temperaturas = 0
quantidade_leituras = 0
quantidade_perigo = 0

print("--- Monitoramento da Estufa ---")
print("Digite -99 para encerrar as leituras.")

while True:
    temp = float(input("Registre a temperatura (°C): "))
    
    # Condição de parada do laço
    if temp == -99:
        break
        
    # Acumuladores e contadores
    soma_temperaturas += temp
    quantidade_leituras += 1
    
    if temp > 35:
        quantidade_perigo += 1

# Validação para evitar divisão por zero caso o usuário digite -99 na primeira vez
if quantidade_leituras > 0:
    media = soma_temperaturas / quantidade_leituras
    print(f"\nResumo:")
    print(f"Temperatura média: {media:.2f}°C")
    print(f"Picos de perigo (> 35°C): {quantidade_perigo} vez(es)")
else:
    print("Nenhuma leitura foi registrada.")