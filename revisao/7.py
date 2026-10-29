
# **7. Avaliação Física de Atletas**
# Um preparador físico precisa avaliar o Índice de Massa Corporal (IMC) de um grupo de atletas. Crie uma função que receba o peso e a altura, calcule o IMC e retorne a classificação (Abaixo do peso, Normal, Sobrepeso, etc.). No programa principal, faça um laço que pergunte os dados de vários atletas. O programa deve parar quando o nome do atleta for "FIM". Ao final, exiba quantos atletas estão na categoria "Normal".

def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

qtd_normal = 0

print("--- Avaliação Física ---")
print("Digite 'FIM' no nome para encerrar.")

while True:
    nome = input("\nNome do atleta: ")
    if nome.upper() == "FIM":
        break
        
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    
    classificacao = calcular_imc(peso, altura)
    print(f"Classificação de {nome}: {classificacao}")
    
    if classificacao == "Normal":
        qtd_normal += 1

print(f"\nTotal de atletas na categoria 'Normal': {qtd_normal}")