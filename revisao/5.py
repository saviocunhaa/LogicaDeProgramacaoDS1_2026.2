
# **5. Simulador de Rendimentos**
# Crie uma função chamada `calcular_juros` que receba um valor inicial, uma taxa de juros mensal e um número de meses. O programa deve usar um laço de repetição dentro ou fora da função para calcular o crescimento do dinheiro mês a mês, aplicando juros compostos. O programa deve imprimir o saldo ao final de cada mês. Se em algum mês o saldo dobrar em relação ao valor inicial, o laço deve ser interrompido e uma mensagem de "Meta Atingida antecipadamente!" deve ser exibida.
def calcular_juros(valor_inicial, taxa_mensal, meses):
    saldo = valor_inicial
    meta = valor_inicial * 2
    
    print("\n--- Evolução do Rendimento ---")
    for mes in range(1, meses + 1):
        # O saldo cresce com a adição dos juros
        saldo += saldo * (taxa_mensal / 100)
        print(f"Mês {mes}: R$ {saldo:.2f}")
        
        # Verifica se atingiu a meta de dobrar o valor
        if saldo >= meta:
            print("Meta Atingida antecipadamente!")
            break

# Programa principal
capital = float(input("Valor inicial a investir: R$ "))
taxa = float(input("Taxa de juros mensal (%): "))
prazo = int(input("Número de meses: "))

calcular_juros(capital, taxa, prazo)