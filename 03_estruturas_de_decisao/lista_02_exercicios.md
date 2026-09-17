# 📜 Lista 02 de Exercícios: Estruturas Condicionais (if, elif, else)

---

### 🔹 Exercício 01: Imposto de Renda de Lisarb
Em um país imaginário denominado Lisarb, a moeda oficial é o Rombus (R$). Leia um valor numérico com duas casas decimais equivalente ao salário de uma pessoa.
* Até R$ 2000.00: **Isento** de imposto.
* De R$ 2000.01 até R$ 3000.00: Imposto de **8%** sobre o valor que exceder R$ 2000.00.
* De R$ 3000.01 até R$ 4500.00: Imposto de **18%** sobre o que ultrapassar R$ 3000.00 + 8% sobre a faixa anterior (R$ 1000.00).
* Acima de R$ 4500.00: Imposto de **28%** sobre o que ultrapassar R$ 4500.00 + impostos das faixas anteriores.

Se o salário for isento, imprima `"Isento"`. Caso contrário, mostre o total do imposto a pagar formatado com duas casas decimais.

---

### 🔹 Exercício 02: Aumento de Salário Escolar
A administração escolar resolveu conceder um reajuste salarial escalonado para os seus colaboradores conforme a tabela:
* Salários de 0.00 até 400.00: Reajuste de **15%**
* Salários de 400.01 até 800.00: Reajuste de **12%**
* Salários de 800.01 até 1200.00: Reajuste de **10%**
* Salários de 1200.01 até 2000.00: Reajuste de **7%**
* Salários acima de 2000.00: Reajuste de **4%**

Leia o salário atual do funcionário e imprima: o novo salário, o valor do reajuste ganho e o percentual aplicado.

---

### 🔹 Exercício 03: Fórmula de Bhaskara e Raízes Reais
Leia 3 valores de ponto flutuante ($A$, $B$ e $C$) correspondentes aos coeficientes de uma equação do segundo grau ($Ax^2 + Bx + C = 0$).
* Se $A = 0$ ou se o discriminante ($\Delta = B^2 - 4AC$) for negativo, o programa não possui raízes reais e deve imprimir: `"Impossivel calcular"`.
* Caso contrário, calcule e mostre as duas raízes $R1$ e $R2$ formatadas com 5 casas decimais.

---

### 🔹 Exercício 04: Cardápio da Lanchonete Escolar
Com base na tabela de preços abaixo, escreva um programa que leia o código numérico do item e a quantidade consumida pelo aluno:

| Código | Especificação | Preço (R$) |
| :---: | :--- | :---: |
| 1 | Cachorro Quente | R$ 4.00 |
| 2 | X-Salada | R$ 4.50 |
| 3 | X-Bacon | R$ 5.00 |
| 4 | Torrada Simples | R$ 2.00 |
| 5 | Refrigerante | R$ 1.50 |

Calcule e mostre o valor total da conta a pagar com mensagem explicativa.

---

### 🔹 Exercício 05: Acesso à Bilheteria do Parque
Crie um sistema de bilheteria que recebe a idade do visitante:
* Se a idade for menor que 12 anos: Bilhete **"Infantil"** (50% de desconto no valor base de R$ 100,00).
* Se a idade for maior ou igual a 60 anos: Bilhete **"Melhor Idade"** (Gratuidade - R$ 0,00).
* Caso contrário: Bilhete **"Integral"** (Valor cheio de R$ 100,00).

Imprima o tipo de bilhete emitido e o valor final a pagar.
