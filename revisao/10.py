# **10. Processamento de Folha de Pagamento**
# Você foi contratado para criar um sistema de folha de pagamento de uma pequena empresa. O programa deve ler o salário bruto de diversos funcionários (pare o cadastro quando for digitado o salário 0).
# Para cada funcionário, o sistema deve calcular dois descontos utilizando **duas funções distintas**:
# *   `calcular_inss(salario_bruto)`: Retorna 8% de desconto se o salário for até R$ 2.000, 10% se for até R$ 4.000, e um teto fixo de R$ 500 para salários superiores.
# *   `calcular_irrf(salario_base)`: O salário base é o salário bruto menos o INSS. A função deve isentar quem ganha até R$ 2.500. Quem ganha acima disso até R$ 5.000 paga 15% sobre o valor que ultrapassar R$ 2.500. Acima de R$ 5.000, paga 27,5% sobre o valor que ultrapassar R$ 2.500.

# Durante o laço de repetição, o programa deve exibir o salário líquido de cada funcionário analisado. Ao encerrar o laço, exiba o total acumulado que a empresa pagará de salários líquidos, o valor total arrecadado de impostos (INSS + IRRF) e o maior salário líquido pago na empresa.

def calcular_inss(salario_bruto):
    if salario_bruto <= 2000:
        return salario_bruto * 0.08
    elif salario_bruto <= 4000:
        return salario_bruto * 0.10
    else:
        return 500.00

def calcular_irrf(salario_base):
    # A regra diz expressamente: imposto "sobre o valor que ultrapassar R$ 2.500"
    if salario_base <= 2500:
        return 0.0
    elif salario_base <= 5000:
        valor_excedente = salario_base - 2500
        return valor_excedente * 0.15
    else:
        valor_excedente = salario_base - 2500
        return valor_excedente * 0.275

# Programa Principal
total_salarios_liquidos = 0.0
total_impostos = 0.0
maior_salario_liquido = 0.0

print("--- Sistema de Folha de Pagamento ---")
print("Digite 0 no salário para encerrar os lançamentos.")

while True:
    bruto = float(input("\nInforme o Salário Bruto: R$ "))
    
    if bruto == 0:
        break
        
    # Processamento passo a passo
    inss = calcular_inss(bruto)
    base_irrf = bruto - inss
    irrf = calcular_irrf(base_irrf)
    
    liquido = bruto - inss - irrf
    
    print(f"Desconto INSS: R$ {inss:.2f}")
    print(f"Desconto IRRF: R$ {irrf:.2f}")
    print(f"Salário Líquido: R$ {liquido:.2f}")
    
    # Acumuladores da empresa
    total_salarios_liquidos += liquido
    total_impostos += (inss + irrf)
    
    # Verificação de maior salário (sem usar listas ou max())
    if liquido > maior_salario_liquido:
        maior_salario_liquido = liquido

print("\n=== RELATÓRIO DA EMPRESA ===")
print(f"Total a pagar em salários líquidos: R$ {total_salarios_liquidos:.2f}")
print(f"Total arrecadado em impostos: R$ {total_impostos:.2f}")
print(f"Maior salário líquido pago: R$ {maior_salario_liquido:.2f}")