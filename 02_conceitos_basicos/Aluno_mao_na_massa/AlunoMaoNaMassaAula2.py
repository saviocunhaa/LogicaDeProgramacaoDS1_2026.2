# TODO: Desenvolva seu algoritmo aqui
# 1. Leia o valor da conta (float)
# 2. Leia o número de pessoas (int)
# 3. Calcule o valor por pessoa
# 4. Imprima formatado usando f-string

valorDaConta = float(input("Digite o Valor da Conta: "))
numeroDePessoas = int(input("Número de Pessoas na mesa: "))
valorPorPessoa =  valorDaConta / numeroDePessoas
print(f"O Valor por pessoa é: {valorPorPessoa:.2f}")