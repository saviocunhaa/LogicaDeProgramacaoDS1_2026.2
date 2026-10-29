
# **4. Votação de Síndico**
# Um condomínio está elegendo o novo síndico. Existem três candidatos (1 - Ana, 2 - João, 3 - Maria). Crie um programa que receba os votos dos moradores indefinidamente, até que o número 0 seja digitado para encerrar a urna. O programa deve rejeitar votos inválidos (números diferentes de 0, 1, 2 e 3), pedindo que o usuário digite novamente. Ao fim, exiba o total de votos de cada candidato e quem foi o vencedor.

votos_ana = 0
votos_joao = 0
votos_maria = 0

print("--- Eleição para Síndico ---")
print("1 - Ana | 2 - João | 3 - Maria | 0 - Encerrar")

while True:
    voto = int(input("Digite seu voto: "))
    
    if voto == 0:
        break
    elif voto == 1:
        votos_ana += 1
    elif voto == 2:
        votos_joao += 1
    elif voto == 3:
        votos_maria += 1
    else:
        print("Voto inválido! Tente novamente.")

print("\n--- Resultado Final ---")
print(f"Ana: {votos_ana} votos")
print(f"João: {votos_joao} votos")
print(f"Maria: {votos_maria} votos")

# Lógica para definir o vencedor sem usar funções prontas como max()
if votos_ana > votos_joao and votos_ana > votos_maria:
    print("Vencedora: Ana!")
elif votos_joao > votos_ana and votos_joao > votos_maria:
    print("Vencedor: João!")
elif votos_maria > votos_ana and votos_maria > votos_joao:
    print("Vencedora: Maria!")
else:
    print("Houve um empate entre os candidatos mais votados.")