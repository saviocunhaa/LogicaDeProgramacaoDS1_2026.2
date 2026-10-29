
# **3. Controle de Qualidade na Fábrica**
# Em uma linha de produção, as peças passam por uma balança. O operador informará o peso de $N$ peças (pergunte ao usuário quantas peças serão pesadas antes de iniciar). Sem utilizar listas, crie um programa que determine e exiba no final qual foi o peso da peça mais pesada e qual foi o peso da peça mais leve que passou pela esteira naquele lote.
print("--- Controle de Qualidade ---")
n_pecas = int(input("Quantas peças serão pesadas neste lote? "))

maior_peso = 0
menor_peso = 0

for i in range(n_pecas):
    peso_atual = float(input(f"Peso da {i+1}ª peça: "))
    
    # Na primeira repetição, a peça é simultaneamente a mais pesada e a mais leve
    if i == 0:
        maior_peso = peso_atual
        menor_peso = peso_atual
    else:
        # Nas demais repetições, comparamos o peso atual com os recordes guardados
        if peso_atual > maior_peso:
            maior_peso = peso_atual
        if peso_atual < menor_peso:
            menor_peso = peso_atual

if n_pecas > 0:
    print("\nRelatório do Lote:")
    print(f"Peça mais pesada: {maior_peso} kg")
    print(f"Peça mais leve: {menor_peso} kg")