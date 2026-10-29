# Lista de Revisão: Lógica de Programação
**Tópicos:** Estruturas de Decisão, Laços de Repetição e Funções.
**Atenção:** Para resolver as questões abaixo, **NÃO** é permitido o uso de estruturas de dados (como vetores, arrays, listas, dicionários, etc.). Todo o processamento deve ser feito utilizando variáveis simples e lógica de laços.

---

## Parte 1: Fixação e Combinação de Conceitos

**1. Calculadora de Frete de E-commerce**
Uma loja virtual precisa de um sistema para calcular o valor do frete. Crie uma função que receba a distância em quilômetros e o tipo de cliente ("Padrão" ou "VIP"). A regra é: R$ 0,50 por km rodado. Se a distância for maior que 100 km, há uma taxa fixa adicional de R$ 15,00. Clientes VIP recebem 20% de desconto no valor final do frete. Peça para o usuário inserir os dados e exiba o resultado utilizando a função criada.

**2. Monitoramento de Temperatura em Estufa**
Um agricultor possui uma estufa e um sensor de temperatura que faz leituras constantes. Escreva um programa que leia continuamente a temperatura registrada (em graus Celsius) até que o usuário digite um valor de parada (por exemplo, -99). Ao final, o programa deve exibir:
* A temperatura média do período.
* Quantas vezes a temperatura ultrapassou a marca de perigo (acima de 35°C).

**3. Controle de Qualidade na Fábrica**
Em uma linha de produção, as peças passam por uma balança. O operador informará o peso de $N$ peças (pergunte ao usuário quantas peças serão pesadas antes de iniciar). Sem utilizar listas, crie um programa que determine e exiba no final qual foi o peso da peça mais pesada e qual foi o peso da peça mais leve que passou pela esteira naquele lote.

**4. Votação de Síndico**
Um condomínio está elegendo o novo síndico. Existem três candidatos (1 - Ana, 2 - João, 3 - Maria). Crie um programa que receba os votos dos moradores indefinidamente, até que o número 0 seja digitado para encerrar a urna. O programa deve rejeitar votos inválidos (números diferentes de 0, 1, 2 e 3), pedindo que o usuário digite novamente. Ao fim, exiba o total de votos de cada candidato e quem foi o vencedor.

**5. Simulador de Rendimentos**
Crie uma função chamada `calcular_juros` que receba um valor inicial, uma taxa de juros mensal e um número de meses. O programa deve usar um laço de repetição dentro ou fora da função para calcular o crescimento do dinheiro mês a mês, aplicando juros compostos. O programa deve imprimir o saldo ao final de cada mês. Se em algum mês o saldo dobrar em relação ao valor inicial, o laço deve ser interrompido e uma mensagem de "Meta Atingida antecipadamente!" deve ser exibida.

**6. Sistema de Tarifas de Táxi**
Crie duas funções distintas: `tarifa_diurna(distancia)` e `tarifa_noturna(distancia)`. A tarifa diurna cobra R$ 4,00 de bandeirada mais R$ 2,50 por km. A noturna cobra R$ 6,00 de bandeirada mais R$ 3,20 por km. O programa principal deve usar um laço para atender vários passageiros ao longo do turno de um motorista. Para cada passageiro, pergunte se a corrida foi de dia (D) ou de noite (N) e a distância. Chame a função adequada e some o valor para o caixa do motorista. O turno acaba quando a distância informada for negativa.

**7. Avaliação Física de Atletas**
Um preparador físico precisa avaliar o Índice de Massa Corporal (IMC) de um grupo de atletas. Crie uma função que receba o peso e a altura, calcule o IMC e retorne a classificação (Abaixo do peso, Normal, Sobrepeso, etc.). No programa principal, faça um laço que pergunte os dados de vários atletas. O programa deve parar quando o nome do atleta for "FIM". Ao final, exiba quantos atletas estão na categoria "Normal".

**8. Caixa de Supermercado**
Faça um programa para registrar os itens da compra de um cliente. O programa deve ler o preço e a quantidade de cada item continuamente. Se o preço digitado for negativo, a compra é encerrada. Se o total da compra ultrapassar R$ 200,00, o sistema deve aplicar um desconto de 10% sobre o total. Exiba o valor bruto, o valor do desconto e o valor final a pagar.

---

## Parte 2: Desafios de Desenvolvimento (Integração de Múltiplos Conceitos)

**9. Caixa Eletrônico (ATM) Avançado**
Desenvolva um simulador de caixa eletrônico. O programa deve exibir um menu contínuo com as opções: 1 - Depositar, 2 - Sacar, 3 - Consultar Saldo, 4 - Sair. 
* O saldo inicial é zero. 
* Crie uma função para lidar com o saque, que receba o saldo atual e o valor desejado. A função deve verificar se há saldo suficiente. Se não houver, deve exibir uma mensagem de erro. 
* **Desafio extra no saque:** Se o saque for aprovado, o programa deve utilizar uma lógica de repetição e decisões (ou restos de divisão) para calcular e exibir a quantidade de notas de R$ 50, R$ 20 e R$ 10 necessárias para entregar o valor, priorizando sempre as notas maiores. (Considere que o caixa só aceita saques múltiplos de 10).

**10. Processamento de Folha de Pagamento**
Você foi contratado para criar um sistema de folha de pagamento de uma pequena empresa. O programa deve ler o salário bruto de diversos funcionários (pare o cadastro quando for digitado o salário 0).
Para cada funcionário, o sistema deve calcular dois descontos utilizando **duas funções distintas**:
*   `calcular_inss(salario_bruto)`: Retorna 8% de desconto se o salário for até R$ 2.000, 10% se for até R$ 4.000, e um teto fixo de R$ 500 para salários superiores.
*   `calcular_irrf(salario_base)`: O salário base é o salário bruto menos o INSS. A função deve isentar quem ganha até R$ 2.500. Quem ganha acima disso até R$ 5.000 paga 15% sobre o valor que ultrapassar R$ 2.500. Acima de R$ 5.000, paga 27,5% sobre o valor que ultrapassar R$ 2.500.

Durante o laço de repetição, o programa deve exibir o salário líquido de cada funcionário analisado. Ao encerrar o laço, exiba o total acumulado que a empresa pagará de salários líquidos, o valor total arrecadado de impostos (INSS + IRRF) e o maior salário líquido pago na empresa.