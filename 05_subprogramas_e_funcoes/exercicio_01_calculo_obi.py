"""
EXERCÍCIO 01: Pontuação OBI (Astro Lume Devs)
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma função nomeada `calcular_pontuacao_total(fase1, fase2, fase3)` com a diretiva `def`
que receba as 3 notas como parâmetros e retorne a pontuação total da equipe.
"""

# TODO: Desenvolva a função e os testes abaixo:

def calcular_pontos_totais(fase1, fase2, fase3):
    total = fase1 + fase2 + fase3
    return total

#testezinho

print(calcular_pontos_totais(80, 40, 77))
print(calcular_pontos_totais(110, 120, 111))
print(calcular_pontos_totais(5, 55, 0))