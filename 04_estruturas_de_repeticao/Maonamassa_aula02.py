soma = 0

while True:
    numero = int(input(" Digite um número inteiro (0 Para encerrar): "))

    if numero == 0:
        break

    soma += numero 

print(f" O valor da soma de todos os números é igual a {soma}")