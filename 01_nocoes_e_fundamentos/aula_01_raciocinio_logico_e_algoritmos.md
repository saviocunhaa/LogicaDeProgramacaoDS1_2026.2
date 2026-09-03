# 🧩 Aula 01: Raciocínio Lógico e Algoritmos

## 1. O que é um Algoritmo?
Um **algoritmo** é uma sequência finita, ordenada e não ambígua de instruções que visam solucionar um determinado problema ou executar uma tarefa específica.

> **Analogia:** Uma receita de bolo, o manual de instruções de montagem de uma mesa ou o passo a passo para trocar o pneu de uma bicicleta são algoritmos do cotidiano.

---

## 2. Os 4 Pilares do Pensamento Computacional

```text
┌─────────────────────────────────────────────────────────────┐
│                 PENSAMENTO COMPUTACIONAL                    │
├───────────────┬─────────────────┬──────────────┬────────────┤
│ 1. Decomposição│ 2. Reconhecimento│ 3. Abstração │ 4. Design  │
│                │    de Padrões   │              │ Algorítmico│
│ Quebrar um    │ Identificar     │ Focar no que │ Criar o    │
│ problema      │ repetições e    │ é essencial  │ passo a    │
│ grande em     │ similaridades   │ e ignorar o  │ passo da   │
│ partes menores│ em problemas    │ detalhe      │ solução    │
│ gerenciáveis  │ passados        │ irrelevante  │            │
└───────────────┴─────────────────┴──────────────┴────────────┘
```

---

## 3. Formas de Representação de Algoritmos

### A. Descrição Narrativa (Linguagem Natural)
* **Passo 1:** Pegar o copo.
* **Passo 2:** Colocar água até a metade.
* **Passo 3:** Adicionar duas colheres de açúcar.
* **Passo 4:** Mexer até dissolver completamente.

### B. Pseudocódigo (Portugol)
```text
Algoritmo CalcularMediaEscolar
Var
    nota1, nota2, media : Real
Início
    Escreva("Digite a primeira nota:")
    Leia(nota1)
    Escreva("Digite a segunda nota:")
    Leia(nota2)
    media <- (nota1 + nota2) / 2
    Se media >= 6.0 Então
        Escreva("Aluno Aprovado!")
    Senão
        Escreva("Aluno em Recuperação.")
    FimSe
Fim
```

### C. Fluxograma
Representação gráfica por símbolos padronizados (retângulos para processos, losangos para decisões, paralelogramos para entrada/saída).
