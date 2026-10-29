# **9. Caixa Eletrônico (ATM) Avançado**
# Desenvolva um simulador de caixa eletrônico. O programa deve exibir um menu contínuo com as opções: 1 - Depositar, 2 - Sacar, 3 - Consultar Saldo, 4 - Sair. 
# * O saldo inicial é zero. 
# * Crie uma função para lidar com o saque, que receba o saldo atual e o valor desejado. A função deve verificar se há saldo suficiente. Se não houver, deve exibir uma mensagem de erro. 
# * **Desafio extra no saque:** Se o saque for aprovado, o programa deve utilizar uma lógica de repetição e decisões (ou restos de divisão) para calcular e exibir a quantidade de notas de R$ 50, R$ 20 e R$ 10 necessárias para entregar o valor, priorizando sempre as notas maiores. (Considere que o caixa só aceita saques múltiplos de 10).


def processar_saque(saldo_atual, valor_saque):
    # Regra 1: Verificar se o valor é múltiplo de 10
    if valor_saque % 10 != 0:
        print("Erro: O caixa só libera notas de R$ 50, R$ 20 e R$ 10.")
        return saldo_atual
    
    # Regra 2: Verificar saldo
    if valor_saque > saldo_atual:
        print("Erro: Saldo insuficiente!")
        return saldo_atual
    
    # Se passou nas regras, fazemos o desconto no saldo
    novo_saldo = saldo_atual - valor_saque
    
    # Lógica de contagem de cédulas (sem usar listas)
    restante = valor_saque
    
    # Quantas vezes 50 cabe no valor restante
    notas_50 = restante // 50  
    restante = restante % 50   # Atualiza o restante com o que sobrou
    
    # Quantas vezes 20 cabe no novo restante
    notas_20 = restante // 20
    restante = restante % 20
    
    # Quantas vezes 10 cabe no novo restante
    notas_10 = restante // 10
    
    print("\n--- Saque Aprovado ---")
    print("Notas entregues:")
    if notas_50 > 0: print(f"{notas_50} nota(s) de R$ 50")
    if notas_20 > 0: print(f"{notas_20} nota(s) de R$ 20")
    if notas_10 > 0: print(f"{notas_10} nota(s) de R$ 10")
    
    return novo_saldo

# Programa Principal
saldo = 0.0

while True:
    print("\n=== BANCO CENTRAL ===")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar Saldo")
    print("4 - Sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        deposito = float(input("Valor do depósito: R$ "))
        if deposito > 0:
            saldo += deposito
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido.")
            
    elif opcao == 2:
        saque = int(input("Valor do saque: R$ "))
        saldo = processar_saque(saldo, saque)
        
    elif opcao == 3:
        print(f"Seu saldo atual é: R$ {saldo:.2f}")
        
    elif opcao == 4:
        print("Obrigado por utilizar nosso banco!")
        break
    else:
        print("Opção inválida.")