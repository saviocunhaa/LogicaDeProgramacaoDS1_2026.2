# 📜 Lista 04 de Exercícios: Funções, Subprogramas e Modularização

---

### 🔹 Exercício 01: Cálculo de Pontuação da OBI (Astro Lume Devs)
A equipe de robótica e programação **Astro Lume Devs** participou de três etapas da Olimpíada Brasileira de Informática (OBI). Crie uma função nomeada `calcular_pontuacao_total(fase1, fase2, fase3)` com a diretiva `def` que receba as três notas como parâmetros e retorne a pontuação final consolidada da equipe.

---

### 🔹 Exercício 02: Modularizando Relatório de Viagem Técnica para Recife
Crie duas funções separadas:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_diesel)`: Retorna o valor gasto com combustível para a viagem.
2. `calcular_custo_alimentacao(qtd_monitores, dias_viagem, diaria_refeicao)`: Retorna o custo total de alimentação da equipe.

No programa principal, solicite os dados necessários, execute as duas funções e imprima o custo operacional consolidado da viagem técnica.

---

### 🔹 Exercício 03: Gerador de Notificações de Vencimento da Cagece
Desenvolva um procedimento (função sem retorno numérico, que apenas executa a exibição formatada com `print`) chamado `emitir_alerta_fatura(nome_cliente, valor_fatura, data_vencimento)`. O procedimento deve imprimir:
```text
Prezado(a) [nome_cliente], sua fatura da Cagece no valor de R$ [valor_fatura] vence no dia [data_vencimento].
```

---

### 🔹 Exercício 04: Investigação de Desconto com Função Lambda
A loja **Casas Paulino** concedeu 15% de desconto à vista em todas as suas categorias de produtos de informática. Escreva uma função anônima (`lambda`) chamada `aplicar_desconto_paulino` que receba o valor original de um produto e retorne instantaneamente o novo valor com o desconto de 15% deduzido.

---

### 🔹 Exercício 05: Gestão de Escopo Global e Local de Inscritos
Desenvolva um programa que possua uma variável global chamada `total_inscritos = 0`. Em seguida, crie uma função `inscrever_aluno(quantidade)` que utilize a instrução `global` para atualizar e incrementar a variável do sistema. Imprima o total de inscritos antes e depois de chamar a função para demonstrar o controle de escopo.
