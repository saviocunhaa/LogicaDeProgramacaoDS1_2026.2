"""
EXERCÍCIO 03: Gerador de Alertas da Cagece
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Desenvolva um procedimento `emitir_alerta_fatura(nome_cliente, valor, data_vencimento)`
que imprima a mensagem:
"Prezado(a) [nome], sua fatura da Cagece no valor de R$ [valor] vence no dia [data]."
"""

# TODO: Desenvolva o procedimento abaixo:

def emitir_alerta_fatura(nome_cliente, valor, data_vencimento):
    print(f"Prezado(a) {nome_cliente}, sua fatura da Cagece no valor de R$ {valor:.2f} vence no dia {data_vencimento}.")


# Testes
emitir_alerta_fatura("Marina Rodrigues ", 125.5, "10/11/2026")
emitir_alerta_fatura("Edson Arantes", 89, "15/11/2026")